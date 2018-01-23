import os
import unittest

from io import StringIO

from entities.customer import Customer
from entities.order_with_bar_codes import OrderWithBarCodes
from exceptions.invalid_object_type_exception import InvalidObjectTypeException
from outputs.console_output import ConsoleOutput
import sys

TEST_ASSETS_DIRECTORY = "/../../tests/assets/outputs/"

class ConsoleOutputTest(unittest.TestCase):

    def test_exception_when_type_is_incorrect(self):
        self.assertRaises(InvalidObjectTypeException, ConsoleOutput.render_result, 1)

    def test_exception_when_items_belongs_to_incorrect_type(self):
        self.assertRaises(InvalidObjectTypeException, ConsoleOutput.render_result, {"1":"Type"})

    def test_when_list_is_empty(self):
        self.__assert_console_result({}, "blank_file.txt")

    def test_when_list_has_a_customer_without_barcodes(self):
        self.__assert_console_result(
            {
                "1": Customer("1", [OrderWithBarCodes("2", "1", [])])
            },
            "customer_without_barcodes.txt"
        )

    def test_when_list_has_a_customer_with_barcodes(self):
        self.__assert_console_result(
            {
                "1": Customer("1", [OrderWithBarCodes("2", "1", [1111,2222,33333])])
            },
            "customer_with_barcodes.txt"
        )

    def test_when_list_has_a_customer_with_multiple_barcodes(self):
        self.__assert_console_result(
            {
                "1" : Customer("1", [OrderWithBarCodes("2", "1", [1111, 2222, 33333])]),
                "2" : Customer("2", [OrderWithBarCodes("5", "2", [4444, 5555, 6666])]),
                "3" : Customer("3", [OrderWithBarCodes("6", "3", [7777, 8888, 9999])]),
            },
            "multiple_customers.txt"
        )

    def __assert_console_result(self, input, output_file):
        file = open(os.path.dirname(__file__) + TEST_ASSETS_DIRECTORY + output_file, "r")
        old_stdout = sys.stdout
        sys.stdout = mystdout = StringIO()
        ConsoleOutput.render_result(input)
        sys.stdout = old_stdout
        self.assertEquals(mystdout.getvalue(), file.read())


if __name__ == '__main__':
    unittest.main()