import unittest
from soda_machine import SodaMachine
from coins import Coin 
from wallet import Wallet

machine = SodaMachine()
x = self.money 

class SodaMachine(unittest.TestCase): #Soda Machine Class 
    """Tests for Soda Machine inventory and register functions"""
    
    def setUp(self):  # each test reruns set up for fresh start 
        """Sets up testing environment"""
        """Instantiates SodaMachine to test"""
        self.SodaMachine = SodaMachine()
        
    #######
    def fill_register(self): # fill register 
        """Test that register is full of coinage"""
        self.SodaMachine = SodaMachine()
        x = self.SodaMachine.fill_register.len(self.money)
        self.assertEqual(self.SodaMachine.fill_register.result.len[x], "Coins")

    #########
    def fill_inventory(self):    # fill inventory 
        self.sodamachine = SodaMachine()
        self.SodaMachine.fill_inventory.len(30)
        self.assertEqual(self.SodaMachine.fill_inventory.result.len[30], "Coins")
        pass 
    
    def get_coin_from_register(self):  # get coin from register
        pass 


    def register_has_coin(self):  # register has coin 
        pass
    
    def determine_change_value(self): # determine change value
        pass 
    
    def calculate_coin_value(self): # calculate coin value  
        pass     
    
    def get_inventory_soda(self): # get inventory soda
        pass  
    
    def return_inventory(self): # return inventory 
        pass 
    
    def deposit_coins_into_register(self):  # deposit coins into register 
        pass 

if __name__ == '__main__':
    unittest.main() 
