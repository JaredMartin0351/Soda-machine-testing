import unittest
from wallet import Wallet
from customer import Customer
from backpack import Backpack
from cans import Cola, RootBeer, OrangeSoda
import coins


class TestGetWalletCoin(unittest.TestCase):
    """Test for get wallet coin in customer class"""
    def setUp(self):
        self.customer = Customer()
        self.wallet = Wallet()
        self.backpack = Backpack()
    
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
        
    def test_get_none(self):
        """Passes in the object that should return none"""
        returned_obj = self.customer.get_wallet_coin('Silver Dollar')
        self.assertIsNone(returned_obj)

    
class TestAddCoinsToWallet(unittest.TestCase):
    """Test to add coins from a list into the wallet object"""
    def setUp(self):
        self.customer = Customer()
        self.wallet = Wallet()
        self.quarter = coins.Quarter()
        self.dime = coins.Dime()
        self.nickel = coins.Nickel()
    
    def test_len_of_coins_list(self):
        """Test len of coin list with addition of 3 more coins to see if orginal len of 88 is updated to 91"""
        coin_list_of_3 = [self.quarter, self.dime, self.nickel]
        self.customer.add_coins_to_wallet(coin_list_of_3)
        coin_list_len = len(self.customer.wallet.money)
        self.assertEqual(coin_list_len,91 )

    def test_len_of_zero_coin_list(self):
        """test len of coin list with 0 aditions to see if return is the same"""
        coin_list_blank = []
        cmpare_list = len(self.customer.wallet.money)
        self.customer.add_coins_to_wallet(coin_list_blank)
        coin_list_blank_len = len(self.customer.wallet.money)
        self.assertEqual(cmpare_list,coin_list_blank_len)
        

class TestAddCanToBackpack(unittest.TestCase):
    """Test to add can to customers backpack"""
    def setUp(self):
        self.customer = Customer()
        self.backpack = Backpack()

    def test_add_can_cola(self):
        """Adding a can object to the list of purchased cans"""
        can = Cola
        self.customer.add_can_to_backpack(can)
        list_len2 = len(self.customer.backpack.purchased_cans)
        self.assertEqual(list_len2,len(self.customer.backpack.purchased_cans))
       
    def test_add_can_rootbeer(self):
        """Adding a can object to the list of purchased cans"""
        can = RootBeer
        self.customer.add_can_to_backpack(can)
        list_len2 = len(self.customer.backpack.purchased_cans)
        self.assertEqual(list_len2,len(self.customer.backpack.purchased_cans))

    def test_add_can_orange_soda(self):
        """Adding a can object to the list of purchased cans"""
        can = OrangeSoda
        self.customer.add_can_to_backpack(can)
        list_len2 = len(self.customer.backpack.purchased_cans)
        self.assertEqual(list_len2,len(self.customer.backpack.purchased_cans))
        
if __name__ == '__main__':
    unittest.main()
    