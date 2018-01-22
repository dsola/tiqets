import unittest

from tiqets.readers.bar_code_reader import BarCodeReader
from pprint import pprint

class BarCodeReaderTest(unittest.TestCase):

    def test_list_is_not_empty(self):
        bar_codes = BarCodeReader.read()
        self.assertGreater(len(bar_codes), 0)

    def test_check_specific_bar_code(self):
        bar_codes = BarCodeReader.read()
        bar_code = bar_codes[2]
        self.assertEquals('11111111113', bar_code.get_reference())
        self.assertEquals('3', bar_code.get_order_id())


if __name__ == '__main__':
    unittest.main()