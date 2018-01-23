class OrderWithBarCodes(object):
    def __init__(self, Id, CustomerId, BarCodes):
        self.__id = Id
        self.__customer_id = CustomerId
        self.__bar_codes=BarCodes

    def get_id(self):
        return self.__id

    def get_bar_codes(self):
        return self.__bar_codes

    def get_customer_id(self):
        return self.__customer_id