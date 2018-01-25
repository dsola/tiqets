import collections

from entities.customer import Customer
from entities.order_with_bar_codes import OrderWithBarCodes
from exceptions.invalid_object_type_exception import InvalidObjectTypeException
from filters.ticket_filter import TicketFilter
from validators.collection_validator import CollectionValidator
from validators.order_validator import OrderValidator


class CustomerExtractor:
    @staticmethod
    def extract(tickets, orders):
        CollectionValidator.validate(tickets)
        CollectionValidator.validate(orders)
        customers = dict()
        for order in orders:
            OrderValidator.validate(order)
            order_with_bar_codes = OrderWithBarCodes(
                order.get_id(),
                order.get_customer_id(),
                TicketFilter.filter_by_order_id(order.get_id(), tickets)
            )

            if (len(order_with_bar_codes.get_bar_code_references()) > 0):
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
