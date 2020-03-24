from abc import abstractmethod


class DataObject:

    def __init__(self,
                 _hash: str = None,
                 _time_stamp: str = None,
                 _amount: str = None,
                 _fee: str = None,
                 ):
        self._hash = _hash
        self._time_stamp = _time_stamp
        self._amount = _amount
        self._fee = _fee

    @property
    def hash(self):
        return self._hash

    @property
    def time_stamp(self):
        return self._time_stamp

    @property
    def amount(self):
        return self._amount

    @property
    def fee(self):
        return self._fee

    @hash.setter
    def hash(self, value):
        self._hash = value

    @time_stamp.setter
    def time_stamp(self, value):
        self._time_stamp = value

    @amount.setter
    def amount(self, value):
        self._amount = value

    @fee.setter
    def fee(self, value):
        self._fee = value

    @abstractmethod
    def info(self):
        """
        get Object's information
        :return:Json json formatted data.
        """
        pass


class Transaction(DataObject):

    def __init__(self,
                 _data: str = None,
                 _status: str = None,
                 _step_limit: str = None,
                 _from_address: str = None,
                 _to_address: str = None,
                 _block_height: str = None,
                 ):
        super().__init__()
        self._data = _data
        self._status = _status
        self._step_limit = _step_limit
        self._from_address = _from_address
        self._to_address = _to_address
        self._block_height = _block_height

    @property
    def data(self):
        return self._data

    @property
    def status(self):
        return self._status

    @property
    def step_limit(self):
        return self._step_limit

    @property
    def from_address(self):
        return self._from_address

    @property
    def to_address(self):
        return self._to_address

    @property
    def block_height(self):
        return self._block_height

    @data.setter
    def data(self, value):
        self._data = value

    @status.setter
    def status(self, value):
        if value in [1, 0]:
            value = bool(value)
        if isinstance(value, bool):
            self._status = value
        else:
            print(f"Plz check status data input data was {value}")
            raise TypeError

    @step_limit.setter
    def step_limit(self, value):
        self._step_limit = value

    @from_address.setter
    def from_address(self, value):
        self._from_address = value

    @to_address.setter
    def to_address(self, value):
        self._to_address = value

    @block_height.setter
    def block_height(self, value):
        self._block_height = value

    def info(self):
        """
        return Transaction info
        :return:
        """
        ret = {
                "txHash":       self._hash,
                "data":         self._data,
                "time_stamp":   self._time_stamp,
                "status":       self._status,
                "amount":       self._amount,
                "fee":          self._fee,
                "step_limit":   self._step_limit,
                "from":         self._from_address,
                "to":           self._to_address,
                "block_height": self._block_height
        }
        return ret


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
                "block_size":    self._block_size,
                "prev_hash":    self._prev_hash,
                "txs":          self._txs,
                "bp":           self._bp,
                "block_height": self._block_height
        }
        return ret

