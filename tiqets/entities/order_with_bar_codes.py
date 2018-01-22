class OrderWithBarCodes(object):
    def __init__(self, Id, BarCodes):
        self.__id = Id
        self.__bar_codes=BarCodes

    def get_id(self):
        return self.__id

    def get_bar_codes(self):
        return self.__bar_codes