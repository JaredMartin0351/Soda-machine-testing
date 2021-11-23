import unittest
from wallet import Wallet
import coins

class TestFillWallet(unittest.TestCase):
    def setUp(self):
        self.wallet = Wallet()
        self.money = []
