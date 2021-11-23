import unittest
import user_interface
from wallet import Wallet
from customer import Customer
from backpack import Backpack
import coins


class TestGetWalletCoin(unittest.TestCase):
    """Test for get wallet coin in customer class"""
    def setUp(self):
        self.customer = Customer()
        self.wallet = Wallet()
    
    
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
    """Test to add coins from a list into the wallet object"""
    def setUp(self):
        self.customer = Customer()
        self.wallet = Wallet()
    
        

    def test_add_quarter(self):
        """Adding a quarter object to the wallet"""
        quarter = coins.Quarter
        coins_list = [quarter]
        self.customer.add_coins_to_wallet(coins_list)
        self.assertEqual(coins_list[0], quarter)
        
    def test_add_dime(self):
        """Adding a dime object to the wallet"""
        dime = coins.Dime
        coins_list = [dime]
        self.customer.add_coins_to_wallet(coins_list)
        self.assertEqual(coins_list[0], dime)
        
    def test_add_nickel(self):
        """Adding a nickel object to the wallet"""
        nickel = coins.Nickel
        coins_list = [nickel]
        self.customer.add_coins_to_wallet(coins_list)
        self.assertEqual(coins_list[0], nickel)
        
    def test_add_penny(self):
        """Adding a penny object to the wallet"""
        penny = coins.Penny
        coins_list = [penny]
        self.customer.add_coins_to_wallet(coins_list)
        self.assertEqual(coins_list[0], penny)
        
if __name__ == '__main__':
    unittest.main()
    
    