class Order(object):
    def __init__(self, Id, CustomerId):
        self.__id = Id
        self.__customer_id=CustomerId

    def get_id(self):
        return self.__id

    def get_customer_id(self):
        return self.__customer_id