from .bech32address import Bech32Address
from defichain.transactions.constants import OPCodes
from defichain.transactions.utils import Converter


class Script(object):

    @staticmethod
    def build_script(data: []) -> str:
        """
        Builds the script with the given parameters

        -> the length of the script is not included at the front of the script

        :param data: script parameters and a decoded address
        :type data: [hex]
        :return: the script that was asked for
        """
        result = ""
        for a in data:
            if len(a) > 2:
                length_address_decode = int(len(a) / 2)
                result += Converter.int_to_hex(length_address_decode, 1) + a
            else:
                result += a
        return result

    @staticmethod
    def script_custom(msg: str) -> bytes:
        op_return = Converter.hex_to_bytes(OPCodes.OP_RETURN)
        msg = Converter.hex_to_bytes(Converter.str_to_hex(msg))
        length_msg = Converter.int_to_bytes(len(msg), 1)
        return op_return + length_msg + msg

    # Deprecated
    @staticmethod
    def p2wpkh(address: str) -> bytes:
        witness_version = Converter.int_to_bytes(0, 1)
        witness_program = Converter.hex_to_bytes(Bech32Address.decode(address))
        witness_length = Converter.int_to_bytes(len(witness_program), 1)
        return witness_version + witness_length + witness_program

    @staticmethod
    def p2wpkh_scriptCode(address: str) -> bytes:
        return bytes.fromhex(f"1976a914{Bech32Address.decode(address)}88ac")
