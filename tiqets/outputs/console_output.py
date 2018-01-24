import collections

from entities.customer import Customer
from exceptions.invalid_object_type_exception import InvalidObjectTypeException

class ConsoleOutput:

    @staticmethod
    def render_customers_with_bar_codes(customers):
        print("--- Customers with orders ---")
        ConsoleOutput.__validate_collection(customers)
        for customer in customers:
            ConsoleOutput.__validate_customer(customer)
            ConsoleOutput.__render_customer(customer)
        print("-----------------------------")

    @staticmethod
    def render_customers_with_ticket_amounts(top_customers):
        print("---Top " + str(len(top_customers)) + " Customers with ticket amounts ---")
        ConsoleOutput.__validate_collection(top_customers)
        for customer in top_customers:
            ConsoleOutput.__validate_customer(customer)
            ConsoleOutput.__render_customer_with_ticket_amounts(customer)
        print("-------------------------------------")

    @staticmethod
    def render_bar_codes_without_orders(bar_codes_without_orders):
        print("--- Bar Codes without orders ---")
        print(len(bar_codes_without_orders))
        print("--------------------------------")

    @staticmethod
    def __validate_collection(customers):
        if not isinstance(customers, collections.Iterable):
            raise InvalidObjectTypeException('The customers argument is not iterable.')

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
    def __render_customer_with_ticket_amounts(customer):
        print(customer.get_id() + ",", end='')
        print(customer.get_total_of_bar_codes())

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