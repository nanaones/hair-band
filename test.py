import unittest
from HairBand.DataObject.DB import Transaction, Block


class TestCustom(unittest.TestCase):

    @staticmethod
    def get_transaction_obj_data_setted():
        _tx = Transaction()
        _tx.hash = "hash"
        _tx.data = "data"
        _tx.time_stamp = "time_stamp"
        _tx.status = "status"
        _tx.amount = "amount"
        _tx.fee = "fee"
        _tx.step_limit = "step_limit"
        _tx.from_address = "_from"
        _tx.to_address = "_to"
        _tx.block_height = "block_height"
        return _tx

    def test_empty_transaction(self):
        _tx = Transaction()
        _info = _tx.info()
        self.assertTrue(len(_info) != 0,
                            msg= f"Check Transaction obj"
                        )

    def test_indata_transaction(self):
        _tx = self.get_transaction_obj_data_setted()
        _info = _tx.info()
        self.assertTrue(len(_info) != 0,
                            msg=f"Check Transaction obj"
                            )
        print(self.test_indata_transaction.__name__, "-- pass")

#TODO: Add test transaction status type Check
#TODO: Add test Block Check


if __name__ == '__main__':
    unittest.main()