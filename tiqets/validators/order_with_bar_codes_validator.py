from entities.order_with_bar_codes import OrderWithBarCodes
from exceptions.invalid_object_type_exception import InvalidObjectTypeException

class OrderWithBarCodesValidator:
    @staticmethod
    def validate(order):
        if not (type(order) is OrderWithBarCodes):
            raise InvalidObjectTypeException('This object is not an OrderWithBarCodes: ' + str(type(order)))