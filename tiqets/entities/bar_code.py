class BarCode(object):
    def __init__(self, Reference, OrderId):
        self.__reference=Reference
        self.__order_id=OrderId

    def get_reference(self):
        return self.__reference

    def get_order_id(self):
        return self.__order_id