import unittest

from exceptions.invalid_directory_path_exception import InvalidDirectoryPathException
from tiqets.readers.order_reader import OrderReader

TEST_ASSETS_DIRECTORY = "/../../tests/assets/orders/"

class BarCodeReaderTest(unittest.TestCase):

    def test_exception_raise_when_directory_not_exists(self):
        self.assertRaises(InvalidDirectoryPathException,OrderReader.read, TEST_ASSETS_DIRECTORY + "not_exists.csv")

    def test_list_is_not_empty(self):
        orders = OrderReader.read(TEST_ASSETS_DIRECTORY + "one_order.csv")
        self.assertGreater(len(orders), 0)

    def test_check_specific_bar_code(self):
        orders = OrderReader.read(TEST_ASSETS_DIRECTORY + "one_order.csv")
        order = orders[0]
        self.__assert_order(order)

    def test_read_multiple_barcodes(self):
        orders = OrderReader.read(TEST_ASSETS_DIRECTORY + "orders.csv")
        self.assertEquals(len(orders), 9)

    def test_orders_without_barcodes_are_not_included(self):
        orders = OrderReader.read(TEST_ASSETS_DIRECTORY + "some_incorrect_orders.csv")
        self.assertEquals(len(orders), 6)

    def test_any_bar_code_repeated_has_been_included(self):
        orders = OrderReader.read(TEST_ASSETS_DIRECTORY + "orders_with_duplicates.csv")
        self.assertEquals(len(orders), 7)

    def __assert_order(self, order):
        self.assertEquals('2', order.get_id())
        self.assertEquals('11', order.get_customer_id())


if __name__ == '__main__':
    unittest.main()