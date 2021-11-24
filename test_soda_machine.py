import unittest
import user_interface
from soda_machine import SodaMachine
from coins import Penny, Nickel, Dime, Quarter
from cans import Cola, OrangeSoda, RootBeer
from wallet import Wallet


machine = SodaMachine()
wallet = Wallet()
coins = (Penny, Nickel, Dime, Quarter)
cans = (Cola, OrangeSoda, RootBeer)


class TestSodaMachine(unittest.TestCase):  # Soda Machine Class
    """Tests for Soda Machine inventory and register functions"""

    def setUp(self):  # each test reruns set up for fresh start
        """Sets up testing environment"""
        """Instantiates SodaMachine to test"""
        self.sodamachine = SodaMachine()

    # test runs
    # def test_fill_register(self): # fill register 
    #     """Test that register is full of coinage"""
    #     """Instantiate a SodaMachine object, test that its register list has a len of 88"""
    #     # self.SodaMachine = SodaMachine()
    #     full =len(machine.register) 
    #     self.assertEqual(full, 88) 

    # test runs
    # def test_fill_inventory(self):    # fill inventory
    #     """Instantiate a SodaMachine object, test that its inventory list has a len of 30"""
    #     # self.sodamachine = SodaMachine()
    #     full_inv = len(machine.inventory)
    #     self.assertEqual(full_inv, 30)
        
    # test runs
    # def test_get_quarter_from_register(self):  # get Quarter from register 
    #     """Test a Quarter can be returned from register"""
    #     coin = machine.get_coin_from_register('Quarter')
    #     self.assertEqual(coin.name, 'Quarter')

    # # test runs
    # def test_get_dime_from_register(self):  # get coin from register
    #     """Test a Dime can be returned from register"""
    #     coin = machine.get_coin_from_register('Dime')
    #     self.assertEqual(coin.name, 'Dime')

    # test runs
    # def test_get_nickel_from_register(self):  # get coin from register
    #     """Test a Nickel can be returned from register"""
    #     coin = machine.get_coin_from_register('Nickel')
    #     self.assertEqual(coin.name, 'Nickel')

    # test runs
    # def test_get_penny_from_register(self):  # get coin from register
    #     """Test a Penny can be returned from register"""
    #     coin = machine.get_coin_from_register('Penny')
    #     self.assertEqual(coin.name, 'Penny')

    # test runs 
    # def test_get_string_from_register(self):  # get coin from register
    #     """Test that passing in a string that is not a valid coin name will return None"""
    #     coin_name = machine.get_coin_from_register('dollar')
    #     self.assertIsNone(coin_name)

    # test runs
    # def test_register_has_quarter(self):  # register has coin
    #     """Test that Quarter will return True"""
    #     register_coin = machine.register_has_coin('Quarter')
    #     self.assertEqual(register_coin, True)

    # test runs 
    # def test_register_has_dime(self):  # register has coin
    #     """Test that Dime will return True"""
    #     register_coin = machine.register_has_coin('Dime')
    #     self.assertEqual(register_coin, True)

    # test runs
    # def test_register_has_nickel(self):  # register has coin
    #     """Test that Nickel will return True"""
    #     register_coin = machine.register_has_coin('Nickel')
    #     self.assertEqual(register_coin, True)

    # test runs 
    # def test_register_has_penny(self):  # register has coin
    #     """Test that Penny will return True"""
    #     register_coin = machine.register_has_coin('Penny')
    #     self.assertEqual(register_coin, True) 

    # # test runs
    # def test_register_has_string(self):  # register has coin
    #     """Test that a non-valid coin name will return False"""
    #     register_coin =machine.register_has_coin('dollar')
    #     self.assertFalse(register_coin) 


    # # def test_determine_change_value(self): # determine change value
    # #     """Test with total payment higher"""
    # #     self.change
    # #     self.assertEqual()



    # # def determine_change_value(self): # determine change value
    # #     """Test with select_soda_price higher"""
    # #     pass

    # # def determine_change_value(self): # determine change value
    # #     """Test with two equal values"""
    # #     pass


# NOT RUNNING
    # def test_calculate_coin_value(self): # calculate coin value
    #     """Instantiate each of the 4 coin types and append them to a list. Pass the list into this
    #         function, ensure the returned values is .41"""
    #     coin_list = []
    #     penny = Penny()
    #     nickel = Nickel()
    #     dime = Dime()
    #     quarter = Quarter()
    #     coin_list.append(penny)
    #     coin_list.append(nickel)
    #     coin_list.append(dime)
    #     coin_list.append(quarter)
    #     coin_calc = self.sodamachine.calculate_coin_value(coin_list)
    #     self.assertEqual(coin_calc.value, .41)


    # def calculate_coin_value(self): # calculate coin value
    #     """Pass in an empty list. Ensure the returned value is 0"""
    #     pass


#######
    # test runs 
    # def test_get_inventory_cola(self):  # get inventory soda
    #     # """Pass in Cola, ensure the returned can has the same name"""
    #     can_inv = self.sodamachine.get_inventory_soda('Cola')
    #     self.assertEqual(can_inv.name, 'Cola')
    
    # test runs
    # def test_get_inventory_orangesoda(self): # get inventory soda 
    #     # """Pass OrangeSoda, ensure the returned can has the same name"""
    #     can_inv = self.sodamachine.get_inventory_soda('Orange Soda')
    #     self.assertEqual(can_inv.name, 'Orange Soda') 
            
    # test runs
    # def test_get_inventory_rootbeer(self): # get inventory soda 
    #     """Pass in RootBeer, ensure the returned can has the same name"""
    #     can_inv = self.sodamachine.get_inventory_soda('Root Beer')
    #     self.assertEqual(can_inv.name, 'Root Beer')
    
    # test runs
    # def test_get_inventory_mountaindew(self): # get inventory soda 
    #     """Pass in Mountain Dew, ensure the returned can has the same name"""
    #     can_inv = self.sodamachine.get_inventory_soda('Mountain Dew') 
    #     self.assertIsNone(can_inv) 



    # def return_inventory(self): # return inventory 
    #     """Instantiate a can and pass it into the method. Test that the len of self.inventory 
    #     is now 31"""
    #     self. Can
    #     self.assertEqual()
    #     pass 
    
    # def deposit_coins_into_register(self):  # deposit coins into register 
    #     """Instantiate each of the 4 coins and append them to a list. Pass the list into the function,
    #     ensure the len of self.register is 92"""
    #     pass 

if __name__ == '__main__':
    unittest.main() 
