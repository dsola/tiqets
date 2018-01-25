from entities.order import Order
from exceptions.invalid_object_type_exception import InvalidObjectTypeException

class OrderValidator:
    @staticmethod
    def validate(order):
        if not (type(order) is Order):
            raise InvalidObjectTypeException('This object is not an order: ' + str(type(order)))