import unittest

from entities.ticket import Ticket
from exceptions.invalid_object_type_exception import InvalidObjectTypeException
from filters.ticket_filter import TicketFilter


class BarCodeFilterTest(unittest.TestCase):

    def test_exception_when_type_is_incorrect(self):
        self.assertRaises(InvalidObjectTypeException, TicketFilter.filter_by_order_id, 1, 2)

    def test_when_list_is_empty(self):
        result = TicketFilter.filter_by_order_id(1, [])
        self.assertEquals(len(result), 0)

    # def test_when_list_contains_an_invalid_bar_code(self):
    #     self.assertRaises(InvalidObjectTypeException, BarCodeFilter.filter_by_order_id, 1, [2])

    def test_when_one_element_exists(self):
        result = TicketFilter.filter_by_order_id(1, [Ticket(1111, 1)])
        self.assertEquals(len(result), 1)

    def test_multiple_elements_but_only_one_exists(self):
        result = TicketFilter.filter_by_order_id(1, [Ticket(1111, 1), Ticket(1111, 2)])
        self.assertEquals(len(result), 1)

    def test_multiple_elements_exists_in_the_list(self):
        result = TicketFilter.filter_by_order_id(1, [Ticket(1111, 1), Ticket(1112, 1), Ticket(1113, 1), Ticket(1113, 2)])
        self.assertEquals(len(result), 3)

if __name__ == '__main__':
    unittest.main()