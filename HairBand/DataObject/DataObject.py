from abc import abstractmethod


class DataObject:

    def __init__(self,
                 _hash: str = None,
                 _time_stamp: str = None,
                 _amount: str = None,
                 _fee: str = None,
                 _status: str = None,
                 _block_height: str = None
                 ):
        self._hash = _hash
        self._time_stamp = _time_stamp
        self._amount = _amount
        self._fee = _fee
        self._status = _status
        self._block_height = _block_height

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

    @property
    def status(self):
        return self._status

    @property
    def block_height(self):
        return self._block_height

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

    @status.setter
    def status(self, value):
        self._status = value

    @block_height.setter
    def block_height(self, value):
        self._block_height = value

    @abstractmethod
    def info(self):
        """
        get Object's information
        :return:Json json formatted data.
        """
        pass
