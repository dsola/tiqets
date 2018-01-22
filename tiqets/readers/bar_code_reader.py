import csv, os
from tiqets.entities.bar_code import BarCode

FILEPATH = "../../assets/barcodes.csv"

class BarCodeReader:

    @staticmethod
    def read(self):
        bar_codes = []
        with open(os.path.abspath(FILEPATH), 'r') as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                bar_codes.append(BarCode(row['barcode'], row['order_id']))

        return bar_codes