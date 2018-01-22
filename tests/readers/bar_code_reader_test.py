import unittest

from exceptions.invalid_directory_path_exception import InvalidDirectoryPathException
from tiqets.readers.bar_code_reader import BarCodeReader

TEST_ASSETS_DIRECTORY = "/../../tests/assets/"

class BarCodeReaderTest(unittest.TestCase):

    def test_exception_raise_when_directory_not_exists(self):
        self.assertRaises(InvalidDirectoryPathException,BarCodeReader.read, TEST_ASSETS_DIRECTORY + "not_exists.csv")

    def test_list_is_not_empty(self):
        bar_codes = BarCodeReader.read(TEST_ASSETS_DIRECTORY + "one_barcode.csv")
        self.assertGreater(len(bar_codes), 0)

    def test_check_specific_bar_code(self):
        bar_codes = BarCodeReader.read(TEST_ASSETS_DIRECTORY + "one_barcode.csv")
        bar_code = bar_codes[0]
        self.assertEquals('11111111111', bar_code.get_reference())
        self.assertEquals('1', bar_code.get_order_id())

    def test_read_multiple_barcodes(self):
        bar_codes = BarCodeReader.read(TEST_ASSETS_DIRECTORY + "barcodes.csv")
        self.assertEquals(len(bar_codes), 7)


if __name__ == '__main__':
    unittest.main()