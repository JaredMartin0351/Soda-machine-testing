import unittest
import user_interface
from wallet import Wallet
from customer import Customer
from backpack import Backpack
import coins


class TestGetWalletCoin(unittest.TestCase):
    def setUp(self):
        self.customer = Customer()
    
    
    def test_get_quarter(self):
        """Passes in the 'Quarter' object, should return the quarter object"""
        returned_coin = self.customer.get_wallet_coin('Quarter')
        self.assertEqual(returned_coin.name, 'Quarter')
        
    def test_get_dime(self):
        """Passes in the 'Dime' object, should return the dime object"""
        returned_coin = self.customer.get_wallet_coin('Dime')
        self.assertEqual(returned_coin.name, 'Dime')
        
    def test_get_nickel(self):
        """Passes in the 'Nickel' object, should return the nickel object"""
        returned_coin = self.customer.get_wallet_coin('Nickel')
        self.assertEqual(returned_coin.name, 'Nickel')
        
    def test_get_penny(self):
        """Passes in the 'Penny' object, should return the penny object"""
        returned_coin = self.customer.get_wallet_coin('Penny')
        self.assertEqual(returned_coin.name, 'Penny')
        

    
    
class TestAddCoinsToWallet(unittest.TestCase):
    def setUp(self):
        self.customer = Customer()
        
        
    def test_add_coins(self):
        coins_list = [coins.Quarter, coins.Dime, coins.Nickel,coins.Penny]
        added_coins = self.customer.add_coins_to_wallet(coins_list)
        self.assertEqual(added_coins, coins_list)
        
#    def test_add_dime(self):
#        added_coin = self.customer.add_coins_to_wallet('Dime')
#        self.assertEqual(added_coin.name, 'Dime')
        
#    def test_add_nickel(self):
#        added_coin = self.customer.add_coins_to_wallet('Nickel')
#        self.assertEqual(added_coin.name, 'Nickel')
        
#    def test_add_penny(self):
#        added_coin = self.customer.add_coins_to_wallet('Penny')
#        self.assertEqual(added_coin.name, 'Penny')
        
if __name__ == '__main__':
    unittest.main()
    
    