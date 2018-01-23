import unittest

from entities.order import Order
from exceptions.invalid_object_type_exception import InvalidObjectTypeException
from filters.order_extractor import OrderExtractor


class OrderExtractorTest(unittest.TestCase):

    def test_exception_when_type_is_incorrect(self):
        self.assertRaises(InvalidObjectTypeException, OrderExtractor.extract_by_customer_id, 1, 2)

    def test_when_list_is_empty(self):
        result = OrderExtractor.extract_by_customer_id(1, [])
        self.assertEquals(len(result), 0)

    def test_when_one_element_exists(self):
        result = OrderExtractor.extract_by_customer_id(1, [Order(1111,1)])
        self.assertEquals(len(result), 1)

    def test_multiple_elements_but_only_one_exists(self):
        result = OrderExtractor.extract_by_customer_id(1, [Order(1111,1), Order(1111, 2)])
        self.assertEquals(len(result), 1)

    def test_multiple_elements_exists_in_the_list(self):
        result = OrderExtractor.extract_by_customer_id(1, [Order(1111,1), Order(1112, 1), Order(1113, 1), Order(1113, 2)])
        self.assertEquals(len(result), 3)

if __name__ == '__main__':
    unittest.main()