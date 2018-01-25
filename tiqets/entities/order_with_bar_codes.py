from entities.order import Order


class OrderWithBarCodes(Order):
    def __init__(self, Id, CustomerId, BarCodes):
        super().__init__(Id, CustomerId)
        self.__bar_codes=BarCodes

    def get_bar_code_references(self):
        return self.__bar_codes