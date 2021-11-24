import unittest
import user_interface
from wallet import Wallet
from customer import Customer
from backpack import Backpack
from cans import Can, Cola, RootBeer
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
        
        
class TestAddCanToBackpack(unittest.TestCase):
    """Test to add can to customers backpack"""
    def setUp(self):
        self.customer = Customer()
        self.backpack = Backpack()
        self.can = Can('Cola', .60)
        
    def test_add_can(self):
        """Adding a can object to the list of purchased cans"""
        can = Can('Cola', .60)
        purchased_cans = [can]
        self.customer.add_can_to_backpack(can)
        self.assertEqual(purchased_cans[0], can)
        
        

#class TestGatherCoinsFromWallet(unittest.TestCase):
#    """Test to gather selected coins from the wallet"""
#    def setUp(self):
#        self.customer = Customer()
#        self.wallet = Wallet()
#        self.backpack = Backpack()
#        customer_payment = []
#        selected_soda = Can('Cola', .60)
        
#    def test_gather_wallet_coins(self):
#        self.customer.gather_coins_from_wallet(self)
        
        
        
        
#    class TestGetUniqueCanNames(unittest.TestCase):
#        def test_can_name_list(self):
#        """Testing the get_unique_can_names method with multiple of the same cans """
#        rootbeer = RootBeer()
#        rootbeer2 = RootBeer()
#        cola = Cola()
#        cola2 = Cola()
#        orangesoda = OrangeSoda()
#        orangesoda2 = OrangeSoda()
#        list_of_can = []
#        list_of_can.append(rootbeer)
#        list_of_can.append(rootbeer2)
#        list_of_can.append(cola)
#        list_of_can.append(cola2)
#        list_of_can.append(orangesoda)
#        list_of_can.append(orangesoda2)
#        can_checker = user_interface.get_unique_can_names(list_of_can)
#        self.assertNotEqual(can_checker,list_of_can)
        
        
class TestCheckBackpack(unittest.TestCase):
    def setUp(self):
        self.customer = Customer()
        self.cola = Cola()
        self.rootbeer = RootBeer()
        
        
    def test_check_backpack(self):
        purchased_cans = [self.cola, self.rootbeer]
        self.customer.check_backpack()
        self.assertEqual(Cola, RootBeer)
        
if __name__ == '__main__':
    unittest.main()
    
    