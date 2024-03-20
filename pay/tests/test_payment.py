from pytest import raises
from pay.payment import pay_order
from pay.order import Order, LineItem
from pay.credit_card import CreditCard


class PaymentProcessorMock:
    def charge(self, card: CreditCard, amount: int):
        print(f"Charging {card} with amount ${amount/100:.2f}.")


def test_pay_order_success():
    order = Order()
    order.line_items.append(LineItem('Test Line Item', 100, 5))
    card = CreditCard(
        card_number="1249190007575069",
        month=12,
        year=2025,
        amount=100,
    )
    pay_order(order, card, PaymentProcessorMock())


def test_pay_order_error():
    order = Order()
    card = CreditCard(
        card_number="1249190007575069",
        month=12,
        year=2025,
        amount=100,
    )
    with raises(ValueError) as error_info:
        pay_order(order, card, PaymentProcessorMock())
    assert "Can't pay an Order with total 0." in str(error_info.value)
 
