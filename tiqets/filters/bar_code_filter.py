import collections

from entities.bar_code import BarCode
from exceptions.invalid_object_type_exception import InvalidObjectTypeException

class BarCodeFilter:
    @staticmethod
    def filter_by_order_id(order_id, bar_codes):
        if not isinstance(bar_codes, collections.Iterable):
            raise InvalidObjectTypeException('The bar_codes argument is not iterable.')

        order_bar_codes = []
        for bar_code_item in bar_codes:
            # BarCodeFilter.__validate_bar_code(bar_code_item)
            if (bar_code_item.get_order_id() == order_id): order_bar_codes.append(bar_code_item.get_reference())

        return order_bar_codes

    @staticmethod
    def __validate_bar_code(bar_code_item):
        if not type(bar_code_item) is BarCode:
            raise InvalidObjectTypeException('The bar_codes list must contain only a Bar Code entities.')
