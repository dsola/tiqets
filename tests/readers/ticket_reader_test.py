import unittest

from exceptions.invalid_directory_path_exception import InvalidDirectoryPathException
from tiqets.readers.ticket_reader import TicketReader

TEST_ASSETS_DIRECTORY = "/../../tests/assets/barcodes/"

class TicketReaderTest(unittest.TestCase):

    def test_exception_raise_when_directory_not_exists(self):
        self.assertRaises(InvalidDirectoryPathException, TicketReader.read, TEST_ASSETS_DIRECTORY + "not_exists.csv")

    def test_list_is_not_empty(self):
        (bar_codes, bar_codes_without_order) = TicketReader.read(TEST_ASSETS_DIRECTORY + "one_barcode.csv")
        self.assertGreater(len(bar_codes), 0)
        self.assertEquals(len(bar_codes_without_order), 0)

    def test_check_specific_bar_code(self):
        (bar_codes, bar_codes_without_order) = TicketReader.read(TEST_ASSETS_DIRECTORY + "one_barcode.csv")
        bar_code = bar_codes[0]
        self.__assert_bar_code(bar_code)

    def test_read_multiple_barcodes(self):
        (bar_codes, bar_codes_without_order) = TicketReader.read(TEST_ASSETS_DIRECTORY + "barcodes.csv")
        self.assertEquals(len(bar_codes), 7)
        self.assertEquals(len(bar_codes_without_order), 0)

    def test_orders_without_barcodes_are_not_included(self):
        (bar_codes, bar_codes_without_order) = TicketReader.read(TEST_ASSETS_DIRECTORY + "some_incorrect_barcodes.csv")
        self.assertEquals(len(bar_codes), 5)
        self.assertEquals(len(bar_codes_without_order), 2)

    def test_any_bar_code_repeated_has_been_included(self):
        (bar_codes, bar_codes_without_order) = TicketReader.read(TEST_ASSETS_DIRECTORY + "barcodes_with_duplicates.csv")
        self.assertEquals(len(bar_codes), 5)
        self.assertEquals(len(bar_codes_without_order), 0)

    def __assert_bar_code(self, bar_code):
        self.assertEquals('11111111111', bar_code.get_bar_code())
        self.assertEquals('1', bar_code.get_order_id())


if __name__ == '__main__':
    unittest.main()