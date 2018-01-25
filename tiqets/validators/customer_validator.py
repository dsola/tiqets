from entities.customer import Customer
from exceptions.invalid_object_type_exception import InvalidObjectTypeException


class CustomerValidator:
    @staticmethod
    def validate(customer):
        if not type(customer) is Customer:
            raise InvalidObjectTypeException('This object is not a customer: ' + str(type(customer)))