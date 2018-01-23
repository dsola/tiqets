import collections

from exceptions.invalid_object_type_exception import InvalidObjectTypeException

class BarCodeFilter:
    @staticmethod
    def filter_by_order_id(order_id, bar_codes):
        if not isinstance(bar_codes, collections.Iterable):
            raise InvalidObjectTypeException('The bar_codes argument is not iterable.')

        order_bar_codes = []
        for bar_code_item in bar_codes:
            if (bar_code_item.get_order_id() == order_id): order_bar_codes.append(bar_code_item.get_reference())

        return order_bar_codes
