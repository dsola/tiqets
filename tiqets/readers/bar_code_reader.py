import csv, os
from tiqets.entities.bar_code import BarCode

FILE_PATH = "/../../assets/barcodes.csv"

class BarCodeReader:

    @staticmethod
    def read():
        bar_codes = []
        with open(os.path.dirname(__file__) + FILE_PATH, 'r') as file:
            reader = csv.reader(file, delimiter=',')
            next(reader)
            for row in reader:
                bar_codes.append(BarCode(row[0], row[1]))

        return bar_codes