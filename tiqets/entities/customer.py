from entities.order_with_bar_codes import OrderWithBarCodes
from exceptions.invalid_object_type_exception import InvalidObjectTypeException


class Customer(object):
    def __init__(self, Id, OrdersWithBarCodes):
        self.__id = Id
        self.__orders_with_bar_codes=OrdersWithBarCodes

    def get_id(self):
        return self.__id

    def get_orders_with_bar_codes(self):
        return self.__orders_with_bar_codes

    def add_order(self, order):
        self.__validate_order(order)
        return self.__orders_with_bar_codes.append(order)

    def get_total_of_bar_codes(self):
        total = 0
        if (len(self.__orders_with_bar_codes) > 0):
            for order in self.__orders_with_bar_codes:
                total += len(order.get_bar_code_references())
        return total


    def __validate_order(self, order):
        if (not type(order) is OrderWithBarCodes):
            raise InvalidObjectTypeException("Invalid order with barcodes included into a customer entity.")