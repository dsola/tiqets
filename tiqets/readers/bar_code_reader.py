import csv, os, logging

from exceptions.invalid_directory_path_exception import InvalidDirectoryPathException
from tiqets.entities.bar_code import BarCode

DEFAULT_FILE_PATH = "/../../assets/barcodes.csv"

class BarCodeReader:

    @staticmethod
    def read(relative_path = ""):
        relative_path = BarCodeReader.__get_relative_path(relative_path)
        bar_codes = []
        bar_codes_without_orders = []
        with open(os.path.dirname(__file__) + relative_path, 'r') as file:
            reader = csv.reader(file, delimiter=',')
            next(reader)
            for row in reader:
                BarCodeReader.__read_row(bar_codes, bar_codes_without_orders, row)

        return (bar_codes, bar_codes_without_orders)

    @staticmethod
    def __read_row(bar_codes, bar_codes_without_orders, row):
        if not row[1]:
            logging.error("The barcode " + row[0] + " doesn't have any order specified.")
            bar_codes_without_orders.append(row)
        else:
            bar_code = BarCode(row[0], row[1])
            if (BarCodeReader.__bar_code_reference_exists(bar_code, bar_codes)):
                logging.error("The bar code with reference " + row[0] + " has been included before")
            else:
                bar_codes.append(bar_code)

    @staticmethod
    def __bar_code_reference_exists(bar_code, bar_codes):
        for bar_code_item in bar_codes:
            if (bar_code_item.get_reference() == bar_code.get_reference()): return True
        return False

    @staticmethod
    def __get_relative_path(relative_path):
        if (relative_path == ""):
            return DEFAULT_FILE_PATH
        elif not (os.path.exists(os.path.dirname(__file__) + relative_path)):
            raise InvalidDirectoryPathException("Any file found in the path " + relative_path)
        return relative_path