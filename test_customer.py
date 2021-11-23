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
    def setUp(self):
        self.customer = Customer()
        self.wallet = Wallet()
    
        
        
#    def test_add_coins_to_wallet(self):
#        self.wallet.money = Wallet()
#        quarter = coins.Quarter()
#        dime = coins.Dime()
#        nickel = coins.Nickel()
#        penny = coins.Penny()
#        coins_list = [quarter, dime, nickel, penny]
#        Customer.add_coins_to_wallet(Customer.wallet, coins_list)
#        self.assertEqual(coins_list)

    def test_add_quarter(self):
        quarter = coins.Quarter()
        coins_list = [quarter]
        added_coin = self.customer.add_coins_to_wallet(self, coins_list)
        self.assertEqual(added_coin, quarter)
        
    def test_add_dime(self):
        dime = coins.Dime()
        coins_list = [dime]
        added_coin = self.customer.add_coins_to_wallet(self, coins_list)
        self.assertEqual(added_coin, dime)
        
    def test_add_nickel(self):
        nickel = coins.Nickel()
        coins_list = [nickel]
        added_coin = self.customer.add_coins_to_wallet(self, coins_list)
        self.assertEqual(added_coin, nickel)
        
    def test_add_penny(self):
        penny = coins.Penny()
        coins_list = [penny]
        added_coin = self.customer.add_coins_to_wallet(self, coins_list)
        self.assertEqual(added_coin, penny)
        
if __name__ == '__main__':
    unittest.main()
    
    