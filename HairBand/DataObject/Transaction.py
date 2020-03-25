from . import DataObject


class Transaction(DataObject):

    def __init__(self,
                 _data: str = None,
                 _status: str = None,
                 _step_used: str = None,
                 _step_price: str = None,
                 _from_address: str = None,
                 _to_address: str = None,
                 _index: str = None,
                 _block_hash: str = None,
                 _cumulative_step_used: str = None
                 ):
        super().__init__()
        self._data = _data
        self._status = _status
        self._step_used = _step_used
        self._from_address = _from_address
        self._to_address = _to_address
        self._index = _index
        self._block_hash = _block_hash
        self._step_price = _step_price
        self._cumulative_step_used = _cumulative_step_used

    @property
    def data(self):
        return self._data

    @property
    def status(self):
        return self._status

    @property
    def step_used(self):
        return self._step_used

    @property
    def from_address(self):
        return self._from_address

    @property
    def to_address(self):
        return self._to_address

    @property
    def index(self):
        return self._index

    @property
    def block_hash(self):
        return self._block_hash

    @property
    def step_price(self):
        return self._step_price

    @property
    def cumulative_step_used(self):
        return self._cumulative_step_used

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

    @step_used.setter
    def step_limit(self, value):
        self._step_used = value

    @from_address.setter
    def from_address(self, value):
        self._from_address = value

    @to_address.setter
    def to_address(self, value):
        self._to_address = value

    @index.setter
    def index(self, value):
        self._index = value

    @block_hash.setter
    def block_hash(self, value):
        self._block_hash = value

    @step_price.setter
    def step_price(self, value):
        self._step_price = value

    @cumulative_step_used.setter
    def cumulative_step_used(self, value):
        self._cumulative_step_used = value

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
