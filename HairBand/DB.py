import pymongo
import configparser
from abc import *


class DataObject(ABCMeta):

    @abstractmethod
    def info(self):
        """
        get Object's information
        :return:Json json formatted data.
        """
        pass


class Transaction(DataObject):

    def __next__(self, _hash, _data):
        self.hash = _hash
        self.data = _data

    def info(self):
        """
        return Transaction info
        :return:
        """
        ret = {
                "txHash": self.hash,
                "data": self.data
        }

        return ret


class Block(DataObject):

    def __next__(self, _hash, _time_stamp, _tx_list):
        self.hash = _hash
        self.time_stamp = _time_stamp
        self.tx_list = _tx_list

    @abstractmethod
    def transaction_list(self):
        pass

    @abstractmethod
    def priv_hash(self):
        """
        get Priviouse Block hash
        :return:
        """
        pass

    @abstractmethod
    def next_hash(self):
        pass