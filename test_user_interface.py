from coins import Quarter,Dime,Nickel,Penny
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


class TestTryParse(unittest.TestCase):
    def test_try_parse_int_withint(self):
        """Testing the try_parse_int method with the in of 10"""
        truenumber = user_interface.try_parse_int(10)
        self.assertEqual(truenumber,10)

    def test_try_parse_int_withstr(self):
        """Testing the try_parse_int method with a str of hello  """
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
class TestGetUniqueCanNames(unittest.TestCase):
    def test_can_name_list(self):
        """Testing the get_unique_can_names method with multiple of the same cans """
        rootbeer = RootBeer()
        rootbeer2 = RootBeer()
        cola = Cola()
        cola2 = Cola()
        orangesoda = OrangeSoda()
        orangesoda2 = OrangeSoda()
        list_of_can = []
        list_of_can.append(rootbeer)
        list_of_can.append(rootbeer2)
        list_of_can.append(cola)
        list_of_can.append(cola2)
        list_of_can.append(orangesoda)
        list_of_can.append(orangesoda2)
        can_checker = user_interface.get_unique_can_names(list_of_can)
        self.assertNotEqual(can_checker,list_of_can)

    def test_can_list_return(self):
        """Testing the get_unique_can_names method with a blank list to see if return is still the same"""
        can_list = []
        check_list = user_interface.get_unique_can_names(can_list)

        self.assertEqual(can_list,check_list)








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


class TestDisplayPaymentValue(unittest.TestCase):
    def test_coin_value(self):
        """Testing the display_payment_value method with all coins that add up to .41"""
        quarter = Quarter()
        dime = Dime()
        nickel = Nickel()
        penny = Penny()
        list_value_41 =[]
        list_value_41.append(quarter)
        list_value_41.append(dime)
        list_value_41.append(nickel)
        list_value_41.append(penny)
        truelist = user_interface.display_payment_value(list_value_41)
        self.assertEqual(truelist , .41)
    def test_empty_list(self):
        """Testing the display_payment_value method with a blank list to get a return value of 0"""
        list_value_0 = []
        list0 = user_interface.display_payment_value(list_value_0)
        self.assertEqual(list0,0)

# display_payment_value – 2 tests
# a. Instantiate each of the 4 coin types and append them to a list. Pass the list into this function, ensure the returned values is .41
# b. Pass in an empty list. Ensure the returned value is 0.

class TestValidateCoinSelection(unittest.TestCase):
    
    def test_coin_sel_1(self):
        """Testing validate_coin_selection with input of (1) to get True and Quarter as a return"""
        quarter_tuple = user_interface.validate_coin_selection(1)
        self.assertEqual(quarter_tuple,(True, "Quarter"))
    
    def test_coin_sel_2(self):
        """Testing validate_coin_selection with input of (2) to get True and Dime as a return"""
        dime_tuple = user_interface.validate_coin_selection(2)
        self.assertEqual(dime_tuple,(True, "Dime"))
    
    def test_coin_sel_3(self):
        """Testing validate_coin_selection with input of (3) to get True and Nickel as a return"""
        nickel_tuple = user_interface.validate_coin_selection(3)
        self.assertEqual(nickel_tuple,(True, "Nickel"))
    
    def test_coin_sel_4(self):
        """Testing validate_coin_selection with input of (4) to get True and Penny as a return"""
        penny_tuple = user_interface.validate_coin_selection(4)
        self.assertEqual(penny_tuple,(True, "Penny"))

    def test_coin_sel_other(self):
        """Testing validate_coin_selection with input other than 1,2,3,4
         to get False and None as a return"""
        otherinput = range(random.randint(5,150))
        other_tuple = user_interface.validate_coin_selection(otherinput)
        self.assertEqual(other_tuple,(False, None))


if __name__ == "__main__":
    unittest.main()
