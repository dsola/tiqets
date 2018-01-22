import csv, os, logging

from entities.order import Order
from exceptions.invalid_directory_path_exception import InvalidDirectoryPathException

DEFAULT_FILE_PATH = "/../../assets/orders.csv"

class OrderReader:

    @staticmethod
    def read(relative_path = ""):
        relative_path = OrderReader.__get_relative_path(relative_path)
        orders = []
        with open(os.path.dirname(__file__) + relative_path, 'r') as file:
            reader = csv.reader(file, delimiter=',')
            next(reader)
            for row in reader:
                OrderReader.__read_row(orders, row)

        return orders

    @staticmethod
    def __read_row(orders, row):
        if (row[1] in [None, ""]):
            logging.error("The order " + row[0] + " doesn't have any customer specified.")
        else:
            order = Order(row[0], row[1])
            if (OrderReader.__order_id_exists(order, orders)):
                logging.error("The order with ID " + row[0] + " must be unique.")
            else:
                orders.append(order)

    @staticmethod
    def __order_id_exists(order, orders):
        for order_item in orders:
            if (order_item.get_id() == order.get_id()): return True
        return False

    @staticmethod
    def __get_relative_path(relative_path):
        if (relative_path == ""):
            return DEFAULT_FILE_PATH
        elif not (os.path.exists(os.path.dirname(__file__) + relative_path)):
            raise InvalidDirectoryPathException("Any file found in the path " + relative_path)
        return relative_path