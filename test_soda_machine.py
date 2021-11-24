import unittest
import user_interface
from soda_machine import SodaMachine
from coins import Penny, Nickel, Dime, Quarter
from cans import Can
from wallet import Wallet


machine = SodaMachine()
wallet = Wallet()
coins = (Penny, Nickel, Dime, Quarter)
# cans = Can()


class SodaMachine(unittest.TestCase):  # Soda Machine Class
    """Tests for Soda Machine inventory and register functions"""

    def setUp(self):  # each test reruns set up for fresh start
        """Sets up testing environment"""
        """Instantiates SodaMachine to test"""
        self.SodaMachine = SodaMachine()

    # test runs
    def test_fill_register(self): # fill register 
        """Test that register is full of coinage"""
        """Instantiate a SodaMachine object, test that its register list has a len of 88"""
        # self.SodaMachine = SodaMachine()
        full =len(machine.register) 
        self.assertEqual(full, 88) 

    ######
    # def test_fill_inventory(self):    # fill inventory
    #     """Instantiate a SodaMachine object, test that its inventory list has a len of 30"""
    #     # self.sodamachine = SodaMachine()
    #     self.SodaMachine.fill_inventory.len(30)
    #     self.assertEqual(self.SodaMachine.fill_inventory.result.len[30], "Coins")
    #     pass

    # def test_get_quarter_from_register(self):  # get Quarter from register 
    #     """Test a Quarter can be returned from register"""
    #     coin = machine.get_coin_from_register('Quarter')
    #     print(coin)
    #     self.assertEqual(coin.name, 'Quarter')

    # def test_get_dime_from_register(self):  # get coin from register
    #     """Test a Dime can be returned from register"""
    #     coin = machine.get_coin_from_register('Dime')
    #     self.assertEqual(coin.name, 'Dime')

    # def test_get_nickel_from_register(self):  # get coin from register
    #     """Test a Nickel can be returned from register"""
    #     coin = machine.get_coin_from_register('Nickel')
    #     self.assertEqual(coin.name, 'Nickel')

    # def test_get_penny_from_register(self):  # get coin from register
    #     """Test a Penny can be returned from register"""
    #     coin = machine.get_coin_from_register('Penny')
    #     self.assertEqual(coin.name, 'Penny')

    # def test_get_string_from_register(self):  # get coin from register
    #     """Test that passing in a string that is not a valid coin name will return None"""
    #     coin = machine.get_coin_from_register('dollar')
    #     self.assertNotEqual(coin.name, False)

    # def test_register_has_quarter(self):  # register has coin
    #     """Test that Quarter will return True"""
    #     register_coin = machine.register_has_coin('Quarter')
    #     self.assertEqual(register_coin, True)

    # def test_register_has_dime(self):  # register has coin
    #     """Test that Dime will return True"""
    #     register_coin = machine.register_has_coin('Dime')
    #     self.assertEqual(register_coin, True)

    # def test_register_has_nickel(self):  # register has coin
    #     """Test that Nickel will return True"""
    #     register_coin = machine.register_has_coin('Nickel')
    #     self.assertEqual(register_coin, True)

    # def test_register_has_penny(self):  # register has coin
    #     """Test that Penny will return True"""
    #     register_coin = machine.register_has_coin('Penny')
    #     self.assertEqual(register_coin, True)

    # def test_register_has_string(self):  # register has coin
    #     """Test that a non-valid coin name will return False"""
    #     register_coin = machine.register_has_coin('Dollar')
    #     self.assertEqual(register_coin, False)

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



    # def test_calculate_coin_value(self): # calculate coin value
    #     """Instantiate each of the 4 coin types and append them to a list. Pass the list into this
    #         function, ensure the returned values is .41"""
    #     coin_list = []
    #     penny = Penny()
    #     nickel = Nickel()
    #     dime = Dime()
    #     quarter = Quarter()
    #     coin_list.append(penny, .01)
    #     coin_list.append(nickel, .05)
    #     coin_list.append(dime, .10)
    #     coin_list.append(quarter, .25)
    #     coin_calc = machine.calculate_coin_value(coin_list)
    #     self.assertNotEqual(coin_calc, coin_list)


    # def calculate_coin_value(self): # calculate coin value
    #     """Pass in an empty list. Ensure the returned value is 0"""
    #     pass



    # def test_get_inventory_cola(self):  # get inventory soda
    #      """Pass in Cola, ensure the returned can has the same name"""
    #     cans = machine.get_inventory_soda('Cola')
    #     self.assertEqual(inventory_soda, True)
     
    # def test_get_inventory_orangesoda(self): # get inventory soda 
    #     """Pass OrangeSoda, ensure the returned can has the same name"""
    #     cans = machine.get_inventory_soda('OrangeSoda')
    #     self.assertEqual(inventory_soda, True) 
    
    # def test_get_inventory_rootbeer(self): # get inventory soda 
    #     """Pass in RootBeer, ensure the returned can has the same name"""
    #     cans = machine.get_inventory_soda('RootBeer')
    #     self.assertEqual(inventory_soda, True)
    
    # def test_get_inventory_mountaindew(self): # get inventory soda 
    #     """Pass in Mountain Dew, ensure the returned can has the same name"""
    #     cans = machine.get_inventory_soda('MountainDew') 
    #     self.assertEqual(inventory_soda, True)
  
    
    
    def return_inventory(self): # return inventory 
        """Instantiate a can and pass it into the method. Test that the len of self.inventory 
        is now 31"""
        self. Can
        self.assertEqual()
        pass 
    
    def deposit_coins_into_register(self):  # deposit coins into register 
        """Instantiate each of the 4 coins and append them to a list. Pass the list into the function,
        ensure the len of self.register is 92"""
        pass 

if __name__ == '__main__':
    unittest.main() 
