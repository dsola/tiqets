import unittest

from entities.customer import Customer
from entities.order_with_bar_codes import OrderWithBarCodes
from exceptions.invalid_object_type_exception import InvalidObjectTypeException
from classifiers.customer_classifier import CustomerClassifier
from exceptions.not_enough_customers_for_classification_exception import NotEnoughCustomersForClassificationException


class CustomerClassifierTest(unittest.TestCase):

    def test_exception_when_type_is_incorrect(self):
        self.assertRaises(InvalidObjectTypeException, CustomerClassifier.get_top_buyers, 1, 2)

    def test_exception_when_list_not_has_customers(self):
        self.assertRaises(NotEnoughCustomersForClassificationException, CustomerClassifier.get_top_buyers, [], 2)

    def test_when_there_is_only_one_customer(self):
        customers = CustomerClassifier.get_top_buyers([Customer("1", [OrderWithBarCodes("1", "1", ["1111"])])], 1)
        self.assertEquals(len(customers), 1)
        self.assertEquals(customers[0].get_id(), "1")
        self.assertEquals(customers[0].get_total_of_bar_codes(), 1)

    def test_when_there_are_multiple_customers(self):
        customers = CustomerClassifier.get_top_buyers(
            [
                Customer("1", [OrderWithBarCodes("1", "1", ["1111"])]),
                Customer("2", [OrderWithBarCodes("2", "2", ["2222","3333"])])
            ], 1)
        self.assertEquals(len(customers), 1)
        self.assertEquals(customers[0].get_id(), "2")
        self.assertEquals(customers[0].get_total_of_bar_codes(), 2)

if __name__ == '__main__':
    unittest.main()