from cans import RootBeer, Cola, OrangeSoda
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


class test_try_parse(unittest.TestCase):
    def test_try_parse_int_withint(self):
        truenumber = user_interface.try_parse_int(10)
        self.assertEqual(truenumber,10)

    def test_try_parse_int_withstr(self):
        string = user_interface.try_parse_int("hello")
        self.assertEqual(string,0)


    
   
# def try_parse_int(value):
#     """Attempts to parse a string into an integer, returns 0 if unable to parse"""
#     try:
#         return int(value)
#     except:
#         return 0

# try_parse_int – 2 tests
# a. Pass in “10”, ensure the int value 10 is returned
# b. Pass in “hello”, ensure 0 is returned
class test_get_unique_can_names(unittest.TestCase):
    def test_can_name(self):
        rootbeer = RootBeer()
        rootbeer2 = RootBeer()
        cola = Cola()
        cola2 = Cola()
        orangesoda = OrangeSoda()
        orangesoda2 = OrangeSoda()








    # def get_unique_can_names(inventory):
    # """Loops through inventory to create a list of all distinct types of sodas available"""
    # unique_cans = []
    # previous_names = []
    # for can in inventory:
    #     if can.name in previous_names:
    #         continue
    #     else:
    #         unique_cans.append(can)
    #         previous_names.append(can.name)
    # return unique_cans



if __name__ == "__main__":
    unittest.main()
