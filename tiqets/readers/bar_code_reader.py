import csv, os, logging

from exceptions.invalid_directory_path_exception import InvalidDirectoryPathException
from tiqets.entities.bar_code import BarCode

DEFAULT_FILE_PATH = "/../../assets/barcodes.csv"

class BarCodeReader:

    @staticmethod
    def read(relative_path = ""):
        relative_path = BarCodeReader.get_relative_path(relative_path)
        bar_codes = []
        with open(os.path.dirname(__file__) + relative_path, 'r') as file:
            reader = csv.reader(file, delimiter=',')
            next(reader)
            for row in reader:
                BarCodeReader.read_row(bar_codes, row)

        return bar_codes

    @staticmethod
    def read_row(bar_codes, row):
        if (row[0] in [None, ""]):
            logging.error("The order " + row[1] + " doesn't have any barcode specified.")
        else:
            bar_code = BarCode(row[0], row[1])
            if (BarCodeReader.bar_code_reference_exists(bar_code, bar_codes)):
                logging.error("The bar code with reference " + row[0] + " has been included before")
            else:
                bar_codes.append(bar_code)

    @staticmethod
    def bar_code_reference_exists(bar_code, bar_codes):
        for bar_code_item in bar_codes:
            if (bar_code_item.get_reference() == bar_code.get_reference()): return True
        return False

    @staticmethod
    def get_relative_path(relative_path):
        if (relative_path == ""):
            return DEFAULT_FILE_PATH
        elif not (os.path.exists(os.path.dirname(__file__) + relative_path)):
            raise InvalidDirectoryPathException("Any file found in the path " + relative_path)
        return relative_path