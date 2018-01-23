from extractors.customer_extractor import CustomerExtractor
from outputs.console_output import ConsoleOutput
from readers.bar_code_reader import BarCodeReader
from readers.order_reader import OrderReader

if __name__ == '__main__':

    orders = OrderReader.read()
    bar_codes = BarCodeReader.read()

    customers = CustomerExtractor.extract(bar_codes, orders)

    ConsoleOutput.render_result(customers)