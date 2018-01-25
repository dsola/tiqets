import csv, os, logging

from exceptions.invalid_directory_path_exception import InvalidDirectoryPathException
from tiqets.entities.ticket import Ticket

DEFAULT_FILE_PATH = "/../../assets/barcodes.csv"

class TicketReader:

    @staticmethod
    def read(relative_path = ""):
        relative_path = TicketReader.__get_relative_path(relative_path)
        tickets = []
        tickets_without_orders = []
        with open(os.path.dirname(__file__) + relative_path, 'r') as file:
            reader = csv.reader(file, delimiter=',')
            next(reader)
            for row in reader:
                TicketReader.__read_row(tickets, tickets_without_orders, row)

        return (tickets, tickets_without_orders)

    @staticmethod
    def __read_row(tickets, tickets_without_orders, row):
        if not row[1]:
            logging.error("The ticket " + row[0] + " doesn't have any order specified.")
            tickets_without_orders.append(row)
        else:
            bar_code = Ticket(row[0], row[1])
            if (TicketReader.__bar_code_reference_exists(bar_code, tickets)):
                logging.error("The ticket with reference " + row[0] + " has been included before")
            else:
                tickets.append(bar_code)

    @staticmethod
    def __bar_code_reference_exists(bar_code, bar_codes):
        for bar_code_item in bar_codes:
            if (bar_code_item.get_bar_code() == bar_code.get_bar_code()): return True
        return False

    @staticmethod
    def __get_relative_path(relative_path):
        if (relative_path == ""):
            return DEFAULT_FILE_PATH
        elif not (os.path.exists(os.path.dirname(__file__) + relative_path)):
            raise InvalidDirectoryPathException("Any file found in the path " + relative_path)
        return relative_path