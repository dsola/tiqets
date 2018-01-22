import csv, os

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
                bar_codes.append(BarCode(row[0], row[1]))

        return bar_codes

    @staticmethod
    def get_relative_path(relative_path):
        if (relative_path == ""):
            return DEFAULT_FILE_PATH
        elif not (os.path.exists(os.path.dirname(__file__) + relative_path)):
            raise InvalidDirectoryPathException("Any file found in the path " + relative_path)
        return relative_path