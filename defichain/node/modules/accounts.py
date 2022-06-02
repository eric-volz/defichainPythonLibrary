from ..util import BuildJson


class Accounts:
    def __init__(self, node):
        self._node = node

    def accounthistorycount(self, owner: str = "mine", no_rewards: bool = None, token: str = None,
                            txtype: str = None) -> int:  # 01
        """
        Returns count of account history.

        :param owner: (optional) Single account ID (CScript or address) or reserved words: "mine" - to list history for all owned accounts or "all" to list whole DB (default = "mine").
        :type owner: str
        :param no_rewards: (optional) Filter out rewards
        :type no_rewards: bool
        :param token: (optional) Filter by token
        :type token: str
        :param txtype: (optional) Filter by transaction type, supported letter from {CustomTxType}
        :type txtype: str
        :return: count (int) Count of account history

        :example:

        >>> node.accounts.accounthistorycount("all", True)
        """
        j = BuildJson()
        j.append("no_rewards", no_rewards)
        j.append("token", token)
        j.append("txtype", txtype)
        return self._node._rpc.call("accounthistorycount", owner, j.build())

    def accounttoaccount(self, _from: str, to: {}, inputs: [{}] = None) -> hash:  # 02
        """
        Creates (and submits to local node and network) a transfer transaction from the specified account to the specfied accounts.
        The first optional argument (may be empty array) is an array of specific UTXOs to spend.

        :param _from: (required) The defi address of sender
        :type _from: str
        :param to: (required)

            .. code-block:: text

                {
                    "address": "str",
                    (string, required) The defi address is the key,
                    the value is amount in amount@token format. If multiple tokens are to be transferred, specify an array ["amount1@t1", "amount2@t2"]
                }

        :type to: json object
        :param inputs: (optional)

            .. code-block:: text

                [{
                    (json object) "txid": "hex",
                    (string, required) The transaction id "vout": n,
                    (numeric, required) The output number
                }, ...]

        :type inputs: json array
        :return: "hash" (string) The hex-encoded hash of broadcasted transaction

        :example:

        >>> node.accounts.accounttoaccount(sender_address, {"address1":"1.0@DFI","address2":["2.0@BTC", "3.0@ETH"]}, [])
        """
        return self._node._rpc.call("accounttoaccount", _from, to, inputs)

    def accounttoutxos(self, _from: str, to: {}, inputs: [{}] = None) -> hash:  # 03
        """
        Creates (and submits to local node and network) a transfer transaction from the specified account to UTXOs.
        The third optional argument (may be empty array) is an array of specific UTXOs to spend.

        :param _from: (required) The defi address of sender
        :type _from: str
        :param to: (required)

            .. code-block:: text

                {
                    "address": "str",
                    (string, required) The defi address is the key,
                    the value is amount in amount@token format. If multiple tokens are to be transferred, specify an array ["amount1@t1", "amount2@t2"]
                }

        :type to: json object
        :param inputs: (optional)

            .. code-block:: text

                [{
                    (json object) "txid": "hex",
                    (string, required) The transaction id "vout": n,
                    (numeric, required) The output number
                }, ...]

        :type inputs: json array
        :return: "hash" (string) The hex-encoded hash of broadcasted transaction

        :example:

        >>> node.accounts.accounttoutxos(sender_address, {"address1":"100@DFI"}, [])
        """
        return self._node._rpc.call("accounttoutxos", _from, to, inputs)

    def executesmartcontract(self, name, amount, address="", inputs=None):  # 04
        return self._node._rpc.call("executesmartcontract", name, amount, address, inputs)

    def futureswap(self, address, amount, destination="", inputs=None):  # 05
        return self._node._rpc.call("futureswap", address, amount, destination, inputs)

    def getaccount(self, owner: str, start: str = None, including_start: bool = None, limit: int = None,
                   indexed_amounts: bool = False) -> "[{...}]":  # 06
        """
        Returns information about account.

        :param owner: (required) Owner address in base58/bech32/hex encoding
        :type owner: str
        :param start: (optional) Optional first key to iterate from, in lexicographical order.Typically it's set to last tokenID from previous request.
        :type start: str
        :param including_start: (optional) If true, then iterate including starting position. False by default
        :type including_start: bool
        :param limit: (optional) Maximum number of orders to return, 100 by default
        :type limit: int
        :param indexed_amounts: (optional) Format of amounts output (default = false): (true: obj = {tokenid:amount,...}, false: array = ["amount@tokenid"...])
        :type indexed_amounts: bool
        :return: [{...}] (array) Json object with order information

        :example:

        >>> node.accounts.getaccount(owner_address)
        """
        pagination = BuildJson()
        pagination.append("start", start)
        pagination.append("including_start", including_start)
        pagination.append("limit", limit)

        return self._node._rpc.call("getaccount", owner, pagination.build(), indexed_amounts)

    def getaccounthistory(self, owner, blockheight, txn):  # 07
        return self._node._rpc.call("getaccounthistory", owner, blockheight, txn)

    def getburninfo(self):  # 08
        return self._node._rpc.call("getburninfo")

    def getpendingfutureswaps(self, address):  # 09
        return self._node._rpc.call("getpendingfutureswaps", address)

    def gettokenbalances(self, start=None, including_start=None, limit=None, indexed_amounts=False, symbol_lookup=False):  # 10
        pagination = BuildJson()
        pagination.append("start", start)
        pagination.append("including_start", including_start)
        pagination.append("limit", limit)

        return self._node._rpc.call("gettokenbalances", pagination.build(), indexed_amounts, symbol_lookup)

    def listaccounthistory(self, owner, maxBlockHeight=None, depth=None, no_rewards=None, token=None, txtype=None,
                           limit=None, txn=None):  # 11
        options = BuildJson()
        options.append("maxBlockHeight", maxBlockHeight)
        options.append("depth", depth)
        options.append("no_rewards", no_rewards)
        options.append("token", token)
        options.append("txtype", txtype)
        options.append("limit", limit)
        options.append("txn", txn)

        return self._node._rpc.call("listaccounthistory", owner, options.build())

    def listaccounts(self, start=None, including_start=None, limit=None, verbose=True, indexed_amounts=False,
                     is_mine_only=False):  # 12
        pagnation = BuildJson()
        pagnation.append("start", start)
        pagnation.append("including_start", including_start)
        pagnation.append("limit", limit)

        return self._node._rpc.call("listaccounts", pagnation.build(), verbose, indexed_amounts, is_mine_only)

    def listburnhistory(self, maxBlockHeight=None, depth=None, token=None, txtype=None, limit=None):  # 13
        options = BuildJson()
        options.append("maxBlockHeight", maxBlockHeight)
        options.append("depth", depth)
        options.append("token", token)
        options.append("txtype", txtype)
        options.append("limit", limit)

        return self._node._rpc.call("listburnhistory", options.build())

    def listcommunitybalances(self):  # 14
        return self._node._rpc.call("listcommunitybalances")

    def listpendingfutureswaps(self) -> {}:  # 15
        """
        Get all pending futures.

        :return: "json" (string) array containing json-objects having following fields:

            .. code-block:: text

                owner : "address"
                values : [{
                    tokenSymbol : "SYMBOL"
                    amount : n.nnnnnnnn
                    destination : "SYMBOL"
                }...]

        :example:

        >>> node.accounts.listpendingfutureswaps()

        """
        return self._node._rpc.call("listpendingfutureswaps")

    def sendtokenstoaddress(self, _from, to, selectionMode="pie"):  # 16
        return self._node._rpc.call("sendtokenstoaddress", _from, to, selectionMode)

    def sendutxosfrom(self, _from, to, amount, change=None):  # 17
        change = _from if change is None else change
        return self._node._rpc.call("sendutxosfrom", _from, to, amount, change)

    def utxostoaccount(self, amounts, inputs=None):  # 18
        return self._node._rpc.call("utxostoaccount", amounts, inputs)

    def withdrawfutureswap(self, address, amount, destination="", inputs=None):  # 19
        return self._node._rpc.call("withdrawfutureswap", address, amount, destination, inputs)
