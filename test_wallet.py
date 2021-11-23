import unittest
from wallet import Wallet
import coins

<<<<<<< HEAD
class Test:
    pass
=======
class TestFillWallet(unittest.TestCase):
    def setUp(self):
        self.wallet = Wallet()
        self.money = []
>>>>>>> 93a8360620debb9f19e9d30804f17b6eb5f52c7f
