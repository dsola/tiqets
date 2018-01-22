import collections

from exceptions.invalid_object_type_exception import InvalidObjectTypeException

class OrderExtractor:
    @staticmethod
    def extract_by_customer_id(customer_id, orders):
        if not isinstance(orders, collections.Iterable):
            raise InvalidObjectTypeException('The orders argument is not iterable.')

        customer_orders = []
        for order_item in orders:
            if (order_item.get_customer_id() == customer_id): customer_orders.append(order_item.get_id())

        return customer_orders
