import collections

from entities.customer import Customer
from exceptions.invalid_object_type_exception import InvalidObjectTypeException

class ConsoleOutput:

    @staticmethod
    def render_result(customers):
        ConsoleOutput.__validate_collection(customers)
        for customer in customers.values():
            ConsoleOutput.__validate_customer(customer)
            ConsoleOutput.__render_customer(customer)

    @staticmethod
    def __validate_collection(customers):
        if not type(customers) is dict:
            raise InvalidObjectTypeException('The customers argument is not a Dictionary.')

    @staticmethod
    def __validate_customer(customer):
        if not type(customer) is Customer:
            raise InvalidObjectTypeException('This element pending to print is not a customer')

    @staticmethod
    def __render_customer(customer):
        for order_with_bar_codes in customer.get_orders_with_bar_codes():
            print(customer.get_id() + ",", end='')
            ConsoleOutput.__render_order(order_with_bar_codes)

    @staticmethod
    def __render_order(order_with_bar_codes):
        print(order_with_bar_codes.get_id() + ",[", end='')
        initial_value = True
        for bar_code in order_with_bar_codes.get_bar_code_references():
            if not(initial_value):
                print(",", end='')
            else:
                initial_value = False
            print(bar_code, end='')
        print("]")