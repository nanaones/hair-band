from abc import *


class DataObject(ABCMeta):

    def __init__(self, hash,
                 data, time_stamp,
                 status, amount, fee):

        self.hash = hash
        self.data = data
        self.time_stamp = time_stamp
        self.status = status
        self.amount = amount
        self.fee = fee

    @abstractmethod
    def info(self):
        """
        get Object's information
        :return:Json json formatted data.
        """
        pass


class Transaction(DataObject):

    def __init__(self,  hash,
                 data, time_stamp,
                 status, amount, fee,
                 step_limit, _from,
                 _to, block_height):
        super().__init__()
        self.hash = hash
        self.data = data
        self.time_stamp = time_stamp
        self.status = status
        self.amount = amount
        self.fee = fee
        self.step_limit = step_limit
        self._from = _from
        self._to = _to
        self.block_height = block_height

    def info(self):
        """
        return Transaction info
        :return:
        """
        super().info()
        ret = {
                "txHash":       self.hash,
                "data":         self.data,
                "time_stamp":   self.time_stamp,
                "status":       self.status,
                "amount":       self.amount,
                "fee":          self.fee,
                "step_limit":   self.step_limit,
                "from":         self._from,
                "to":           self._to,
                "block_height": self.block_height
        }
        return ret


class Block(DataObject):

    def __init__(self,  hash,
                 time_stamp, prev_hash,
                 amount, fee,
                 bp, block_size,
                 txs, block_height):

        super().__init__()
        self.hash = hash
        self.time_stamp = time_stamp
        self.block_height = block_height
        self.bp = bp
        self.txs = txs
        self.prev_hash = prev_hash
        self.block_size = block_size
        self.fee = fee
        self.amount = amount

    def info(self):
        """
        return Transaction info
        :return:
        """
        super().info()
        ret = {
                "txHash":       self.hash,
                "time_stamp":   self.time_stamp,
                "status":       self.status,
                "amount":       self.amount,
                "fee":          self.fee,
                "block_size":    self.block_size,
                "prev_hash":    self.prev_hash,
                "txs":          self.txs,
                "bp":           self.bp,
                "block_height": self.block_height
        }
        return ret

