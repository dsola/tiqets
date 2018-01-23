class Customer(object):
    def __init__(self, Id, OrdersWithBarCodes):
        self.__id = Id
        self.__orders_with_bar_codes=OrdersWithBarCodes

    def get_id(self):
        return self.__id

    def get_orders_with_bar_codes(self):
        return self.__orders_with_bar_codes