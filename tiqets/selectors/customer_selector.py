import collections
from operator import itemgetter

from entities.customer import Customer
from exceptions.invalid_object_type_exception import InvalidObjectTypeException

class CustomerSelector:

    @staticmethod
    def get_top_buyers(customers, number_of_elements):

        if not isinstance(customers, collections.Iterable):
            raise InvalidObjectTypeException('The input of the CustomerSelector must be a list.')

        index = range(0, number_of_elements)
        top_customers = sorted(customers, key=Customer.get_total_of_bar_codes, reverse=True)
        return itemgetter(*index)(top_customers)

    @staticmethod
    def __validate_customer(customer):
        if not type(customer) is Customer:
            raise InvalidObjectTypeException('The customers list must contain only Customer entities.')
