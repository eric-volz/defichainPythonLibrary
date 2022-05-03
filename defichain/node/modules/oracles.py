from ..util import BuildJson
from defichain.exceptions.InternalServerError import InternalServerError


class Oracles:
    def __init__(self, node):
        self._node = node

    def appointoracle(self, address, pricefeeds, weightage, inputs=None):  # 01
        return self._node._rpc.call("appointoracle", address, pricefeeds, weightage, inputs)

    def getfixedintervalprice(self, token, currency):  # 02
        return self._node._rpc.call("getfixedintervalprice", f"{token}/{currency}")

    def getfutureswapblock(self):  # 03
        return self._node._rpc.call("getfutureswapblock")

    def getoracledata(self, oracleid):  # 04
        return self._node._rpc.call("getoracledata", oracleid)

    def getprice(self, token, currency):  # 05
        request = BuildJson()
        request.append("currency", currency)
        request.append("token", token)
        return self._node._rpc.call("getprice", request.build())

    def listfixedintervalprices(self, start_token=None, start_currency=None, limit=None):  # 06
        if start_token and not start_currency or not start_token and start_currency:
            raise InternalServerError(-1, "if one of the first two parameters is given, the other must also be given")
        pagination = BuildJson()
        pagination.append("start", f"{start_token}/{start_currency}")
        pagination.append("limit", limit)
        return self._node._rpc.call("listfixedintervalprices", pagination.build())

    def listlatestrawprices(self, token, currency, start=None, including_start=None, limit=None):  # 07
        request = BuildJson()
        request.append("currency", currency)
        request.append("token", token)

        pagination = BuildJson()
        pagination.append("start", start)
        pagination.append("including_start", including_start)
        pagination.append("limit", limit)
        return self._node._rpc.call("listlatestrawprices", request.build(), pagination.build())

    def listoracles(self, start=None, including_start=None, limit=None):  # 08
        pagination = BuildJson()
        pagination.append("start", start)
        pagination.append("including_start", including_start)
        pagination.append("limit", limit)
        return self._node._rpc.call("listoracles", pagination.build())

    def listprices(self, start=None, including_start=None, limit=None):  # 09
        pagination = BuildJson()
        pagination.append("start", start)
        pagination.append("including_start", including_start)
        pagination.append("limit", limit)
        return self._node._rpc.call("listprices", pagination.build())

    def removeoracle(self, oracleid, inputs=None):  # 10
        return self._node._rpc.call("removeoracle", oracleid, inputs)

    def setoracledata(self, oracleid, timestamp, prices, inputs=None):  # 11
        return self._node._rpc.call("setoracledata", oracleid, timestamp, prices, inputs)

    def updateoracle(self, oracleid, address, pricefeeds, weightage, inputs=None):  # 12
        return self._node._rpc.call("updateoracle", oracleid, address, pricefeeds, weightage, inputs)
