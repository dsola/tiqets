from extractors.customer_extractor import CustomerExtractor
from outputs.console_output import ConsoleOutput
from readers.ticket_reader import TicketReader
from readers.order_reader import OrderReader
from classifiers.customer_classifier import CustomerClassifier

if __name__ == '__main__':

    orders = OrderReader.read()
    (bar_codes, bar_codes_without_orders) = TicketReader.read()

    customers = CustomerExtractor.extract(bar_codes, orders)
    ConsoleOutput.render_customers_with_bar_codes(customers.values())

    top_customers = CustomerClassifier.get_top_buyers(customers.values(), 5)
    ConsoleOutput.render_customers_with_ticket_amounts(top_customers)

    ConsoleOutput.render_bar_codes_without_orders(bar_codes_without_orders)