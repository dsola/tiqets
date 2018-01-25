from validators.order_with_bar_codes_validator import OrderWithBarCodesValidator


class Customer(object):
    def __init__(self, Id, OrdersWithBarCodes):
        self.__id = Id
        self.__orders_with_bar_codes=OrdersWithBarCodes

    def get_id(self):
        return self.__id

    def get_orders_with_bar_codes(self):
        return self.__orders_with_bar_codes

    def add_order(self, order):
        OrderWithBarCodesValidator.validate(order)
        return self.__orders_with_bar_codes.append(order)

    def get_total_of_bar_codes(self):
        total = 0
        if (len(self.__orders_with_bar_codes) > 0):
            for order in self.__orders_with_bar_codes:
                total += len(order.get_bar_code_references())
        return total