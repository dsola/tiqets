import collections

from entities.customer import Customer
from entities.order_with_bar_codes import OrderWithBarCodes
from exceptions.invalid_object_type_exception import InvalidObjectTypeException
from filters.bar_code_filter import BarCodeFilter


class CustomerExtractor:
    @staticmethod
    def extract(bar_codes, orders):
        if not isinstance(orders, collections.Iterable):
            raise InvalidObjectTypeException('The orders argument is not iterable.')

        customers = dict()
        for order in orders:
            order_with_bar_codes = OrderWithBarCodes(
                order.get_id(),
                order.get_customer_id(),
                BarCodeFilter.filter_by_order_id(order.get_id(), bar_codes)
            )
            CustomerExtractor.__include_customer_into_the_collection(customers, order_with_bar_codes)

        return customers

    @staticmethod
    def __include_customer_into_the_collection(customers, order_with_bar_codes):
        customer_id = order_with_bar_codes.get_customer_id()
        if (customer_id in customers.keys()):
            CustomerExtractor.__update_customer(customers, order_with_bar_codes)
        else:
            CustomerExtractor.__append_customer(customers, order_with_bar_codes)

    @staticmethod
    def __append_customer(customers, order_with_bar_codes):
        customer_id = order_with_bar_codes.get_customer_id()
        customers[customer_id] = Customer(customer_id, [order_with_bar_codes])

    @staticmethod
    def __update_customer(customers, order_with_bar_codes):
        customer = customers.get(order_with_bar_codes.get_customer_id())
        customer.add_order(order_with_bar_codes)
        customers[customer.get_id()] = customer
