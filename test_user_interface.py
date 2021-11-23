import random
import unittest
import user_interface
class Testuserinterface(unittest.TestCase):


    def test_validate_menu_input_1(self):
        """Test the validation for user input of 1"""
        selection = user_interface.validate_main_menu(1)
        self.assertEqual(selection, (True,1))

    def test_validate_menu_input_2(self):
        """Test the validation for user input of 2"""
        selection = user_interface.validate_main_menu(2)
        self.assertEqual(selection, (True,2))

    def test_validate_menu_input_3(self):
        """Test the validation for user input of 3"""
        selection = user_interface.validate_main_menu(3)
        self.assertEqual(selection, (True,3))
    
    def test_validate_menu_input_4(self):
        """Test the validation for user input of 4"""
        selection = user_interface.validate_main_menu(4)
        self.assertEqual(selection, (True,4))

    def test_validate_menu_input_false(self):
        """Test the validation for user input that isnt 1,2,3,4 """
        badinput = ((range(random.randint(5,150))))
        selection = user_interface.validate_main_menu(badinput)
        self.assertEqual(selection, (False,None))
# validate_main_menu – 5 tests
# a. Pass in each number 1-4, ensure the tuple of (True, number) is returned
# b. Pass in a different number, ensure (False, None) is returned


class test_try_parse(unit)

if __name__ == "__main__":
    unittest.main()
