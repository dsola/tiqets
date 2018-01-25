import collections
from exceptions.invalid_object_type_exception import InvalidObjectTypeException

class CollectionValidator:
    @staticmethod
    def validate(collection):
        if not isinstance(collection, collections.Iterable):
            raise InvalidObjectTypeException('The bar_codes argument is not iterable.')