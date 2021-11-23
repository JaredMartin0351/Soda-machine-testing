from cans import Cola, OrangeSoda, RootBeer
import unittest


class TestCanName(unittest.TestCase):
    
    def test_cola_name(self):        
        cola = Cola()
        self.assertEqual('Cola', cola.name)
        
    def test_orange_soda_name(self):        
        orangesoda = OrangeSoda()
        self.assertEqual('Orange Soda', orangesoda.name)
        
    def test_root_beer_name(self):        
        rootbeer = RootBeer()
        self.assertEqual('Root Beer', rootbeer.name)
        
if __name__ == '__main__':
    unittest.main()
        