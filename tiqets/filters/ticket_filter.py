from validators.collection_validator import CollectionValidator
from validators.ticket_validator import TicketValidator


class TicketFilter:
    @staticmethod
    def filter_by_order_id(order_id, tickets):
        CollectionValidator.validate(tickets)

        order_bar_codes = []
        for ticket in tickets:
            # TicketValidator.validate(ticket)
            if (ticket.get_order_id() == order_id): order_bar_codes.append(ticket.get_bar_code())

        return order_bar_codes