from coins import Dime, Quarter, Nickel, Penny
import unittest


class TestCoinName(unittest.TestCase):
    """Test the names of the coins objects in the Coin class"""
    
    def test_quarter_name(self):        
        quarter = Quarter()
        self.assertEqual('Quarter', quarter.name)
        
    def test_dime_name(self):        
        dime = Dime()
        self.assertEqual('Dime', dime.name)
        
    def test_nickel_name(self):        
        nickel = Nickel()
        self.assertEqual('Nickel', nickel.name)
        
    def test_penny_name(self):        
        penny = Penny()
        self.assertEqual('Penny', penny.name)
        
if __name__ == '__main__':
    unittest.main()
        
