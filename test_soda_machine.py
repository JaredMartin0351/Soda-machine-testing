import unittest
from soda_machine import SodaMachine

class SodaMachine(unittest.TestCase): #Soda Machine Class 
    """Tests for Soda Machine inventory and register functions"""
    
    def setUp(self):  # each test reruns set up for fresh start 
        """Sets up testing environment"""
        """Instantiates SodaMachine to test"""
    
    def fill_register(self): # fill register 
        """Test that register is full of coinage"""
        self....('Quarter')
        self.assertEqual('Quarter', self.soda_machine.register[1])
        
    def fill_inventory(self):    # fill inventory 
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
