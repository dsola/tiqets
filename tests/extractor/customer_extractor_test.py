import unittest

from entities.bar_code import BarCode
from entities.order import Order
from exceptions.invalid_object_type_exception import InvalidObjectTypeException
from extractors.customer_extractor import CustomerExtractor

BARCODE_REFERENCE = "1111"
ORDER_ID = "1"
CUSTOMER_ID = "1"

BARCODE_REFERENCE_2 = "2222"
ORDER_ID_2 = "2"
CUSTOMER_ID_2 = "2"


class CustomerExtractorTest(unittest.TestCase):

    def test_exception_when_orders_are_not_a_collection(self):
        self.assertRaises(InvalidObjectTypeException, CustomerExtractor.extract, 1, [])

    def test_exception_when_bar_codes_are_not_a_collection(self):
        self.assertRaises(InvalidObjectTypeException, CustomerExtractor.extract, [], 1)

    def test_exception_when_orders_contains_and_invalid_type(self):
        self.assertRaises(InvalidObjectTypeException, CustomerExtractor.extract, [], [1])

    def test_when_has_one_order_with_no_barcodes(self):
        orders = [ Order("1", "1") ]
        bar_codes = [ BarCode("1111", "2")]
        result = CustomerExtractor.extract(bar_codes, orders)
        self.assertEquals(len(result.values()), 0)

    def test_when_has_one_order_with_one_barcode(self):
        orders = [Order(ORDER_ID, CUSTOMER_ID)]
        bar_codes = [BarCode(BARCODE_REFERENCE, ORDER_ID)]
        result = CustomerExtractor.extract(bar_codes, orders)
        self.assertEquals(len(result.values()), 1)
        self.__assert_customer(
            result.get(CUSTOMER_ID),
            CUSTOMER_ID,
            0,
            ORDER_ID,
            BARCODE_REFERENCE
        )

    def test_when_has_multiple_orders_with_multiple_barcodes(self):
        orders = [Order(ORDER_ID, CUSTOMER_ID), Order(ORDER_ID_2, CUSTOMER_ID_2)]
        bar_codes = [BarCode(BARCODE_REFERENCE, ORDER_ID), BarCode(BARCODE_REFERENCE_2, ORDER_ID_2)]
        result = CustomerExtractor.extract(bar_codes, orders)
        self.assertEquals(len(result.values()), 2)
        self.__assert_customer(
            result.get(CUSTOMER_ID),
            CUSTOMER_ID,
            0,
            ORDER_ID,
            BARCODE_REFERENCE
        )

        self.__assert_customer(
            result.get(CUSTOMER_ID_2),
            CUSTOMER_ID_2,
            0,
            ORDER_ID_2,
            BARCODE_REFERENCE_2
        )

    def test_when_has_multiple_orders_with_multiple_barcodes_for_the_same_customer(self):
        orders = [Order(ORDER_ID, CUSTOMER_ID), Order(ORDER_ID_2, CUSTOMER_ID)]
        bar_codes = [BarCode(BARCODE_REFERENCE, ORDER_ID), BarCode(BARCODE_REFERENCE_2, ORDER_ID_2)]
        result = CustomerExtractor.extract(bar_codes, orders)
        self.assertEquals(len(result.values()), 1)
        self.__assert_customer(
            result.get(CUSTOMER_ID),
            CUSTOMER_ID,
            0,
            ORDER_ID,
            BARCODE_REFERENCE
        )

        self.__assert_customer(
            result.get(CUSTOMER_ID),
            CUSTOMER_ID,
            1,
            ORDER_ID_2,
            BARCODE_REFERENCE_2
        )

    def __assert_customer(self, customer, customer_id, order_position, order_id, bar_code_reference):
        self.assertEquals(customer.get_id(), customer_id)
        order_with_bar_codes = customer.get_orders_with_bar_codes()[order_position]
        self.assertEquals(order_with_bar_codes.get_id(), order_id)
        bar_code = order_with_bar_codes.get_bar_code_references()[0]
        self.assertEquals(bar_code, bar_code_reference)

if __name__ == '__main__':
    unittest.main()