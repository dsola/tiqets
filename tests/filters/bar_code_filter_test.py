import unittest

from entities.bar_code import BarCode
from exceptions.invalid_object_type_exception import InvalidObjectTypeException
from filters.bar_code_filter import BarCodeFilter


class BarCodeFilterTest(unittest.TestCase):

    def test_exception_when_type_is_incorrect(self):
        self.assertRaises(InvalidObjectTypeException, BarCodeFilter.filter_by_order_id, 1, 2)

    def test_when_list_is_empty(self):
        result = BarCodeFilter.filter_by_order_id(1, [])
        self.assertEquals(len(result), 0)

    def test_when_one_element_exists(self):
        result = BarCodeFilter.filter_by_order_id(1, [BarCode(1111, 1)])
        self.assertEquals(len(result), 1)

    def test_multiple_elements_but_only_one_exists(self):
        result = BarCodeFilter.filter_by_order_id(1, [BarCode(1111, 1), BarCode(1111, 2)])
        self.assertEquals(len(result), 1)

    def test_multiple_elements_exists_in_the_list(self):
        result = BarCodeFilter.filter_by_order_id(1, [BarCode(1111, 1), BarCode(1112, 1), BarCode(1113, 1), BarCode(1113, 2)])
        self.assertEquals(len(result), 3)

if __name__ == '__main__':
    unittest.main()