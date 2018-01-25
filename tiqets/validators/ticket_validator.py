from entities.ticket import Ticket
from exceptions.invalid_object_type_exception import InvalidObjectTypeException

class TicketValidator:
    @staticmethod
    def validate(ticket):
        if not (type(ticket) is Ticket):
            raise InvalidObjectTypeException('The following object is not a Ticket: ' + str(type(ticket)))
