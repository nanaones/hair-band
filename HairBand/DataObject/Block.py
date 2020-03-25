from . import DataObject


class Block(DataObject):

    def __init__(self,
                 _block_height: str = None,
                 _bp: str = None,
                 _txs: str = None,
                 _prev_hash: str = None,
                 _block_size: str = None,
                 ):
        super().__init__()
        self._block_height = _block_height
        self._bp = _bp
        self._txs = _txs
        self._prev_hash = _prev_hash
        self._block_size = _block_size

    @property
    def block_height(self):
        return self._block_height

    @property
    def bp(self):
        return self._bp

    @property
    def txs(self):
        return self._txs

    @property
    def prev_hash(self):
        return self._prev_hash

    @property
    def block_size(self):
        return self._block_size

    @block_height.setter
    def block_height(self, value):
        self._block_height = value

    @bp.setter
    def bp(self, value):
        self._bp = value

    @txs.setter
    def txs(self, value):
        self._txs = value

    @prev_hash.setter
    def prev_hash(self, value):
        self._prev_hash = value

    @block_size.setter
    def block_size(self, value):
        self._block_size = value

    def info(self):
        """
        return Transaction info
        :return:
        """
        ret = {
                "txHash":       self._hash,
                "time_stamp":   self._time_stamp,
                "amount":       self._amount,
                "fee":          self._fee,
                "block_size":   self._block_size,
                "prev_hash":    self._prev_hash,
                "txs":          self._txs,
                "bp":           self._bp,
                "block_height": self._block_height
        }
        return ret

