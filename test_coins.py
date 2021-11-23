from coins import Quarter
import unittest


class Test_QuarterName(unittest.TestCase):
    
    def test_quarter_name(self):        
        quarter = Quarter()
        self.assertEqual('Quarter', quarter.name)
        
