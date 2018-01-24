from extractors.customer_extractor import CustomerExtractor
from outputs.console_output import ConsoleOutput
from readers.bar_code_reader import BarCodeReader
from readers.order_reader import OrderReader
from selectors.customer_selector import CustomerSelector

if __name__ == '__main__':

    orders = OrderReader.read()
    bar_codes = BarCodeReader.read()

    customers = CustomerExtractor.extract(bar_codes, orders)
    ConsoleOutput.render_customers_with_bar_codes(customers.values())

    top_customers = CustomerSelector.get_top_buyers(customers.values(), 5)
    ConsoleOutput.render_customers_with_ticket_amounts(top_customers)