import collections
from operator import itemgetter

from entities.customer import Customer
from exceptions.invalid_object_type_exception import InvalidObjectTypeException
from exceptions.not_enough_customers_for_classification_exception import NotEnoughCustomersForClassificationException


class CustomerClassifier:

    @staticmethod
    def get_top_buyers(customers, number_of_elements):

        CustomerClassifier.__validate_collection(customers)
        CustomerClassifier.__validate_number_of_elements(customers, number_of_elements)

        index = range(0, number_of_elements)
        ranked_customers = sorted(customers, key=Customer.get_total_of_bar_codes, reverse=True)

        return CustomerClassifier.__get_top_customers(index, ranked_customers)

    @staticmethod
    def __get_top_customers(index, ranked_customers):
        top_customers = itemgetter(*index)(ranked_customers)
        if not isinstance(top_customers, collections.Iterable):
            return [top_customers]
        return top_customers

    @staticmethod
    def __validate_number_of_elements(customers, number_of_elements):
        if len(customers) < number_of_elements:
            raise NotEnoughCustomersForClassificationException(
                "There are less customers than number of elements to display: " +
                str(len(customers)) + " and " + str(number_of_elements)
            )

    @staticmethod
    def __validate_collection(customers):
        if not isinstance(customers, collections.Iterable):
            raise InvalidObjectTypeException('The input of the CustomerSelector must be a list.')

    @staticmethod
    def __validate_customer(customer):
        if not type(customer) is Customer:
            raise InvalidObjectTypeException('The customers list must contain only Customer entities.')
