from datetime import date
from pytest import raises, fixture
from pay.payment import pay_order
from pay.order import Order, LineItem
from pay.credit_card import CreditCard


class PaymentProcessorMock:
    def charge(self, card: CreditCard, amount: int):
        print(f"Charging {card} with amount ${amount/100:.2f}.")


@fixture
def card() -> CreditCard:
    year = date.today().year + 2
    return CreditCard(
        card_number="1249190007575069",
        month=12,
        year=year,
        amount=100,
    )


def test_pay_order_success(card: CreditCard):
    order = Order()
    order.line_items.append(LineItem('Test Line Item', 100, 5))
    pay_order(order, card, PaymentProcessorMock())


def test_pay_order_error(card: CreditCard):
    order = Order()
    with raises(ValueError) as error_info:
        pay_order(order, card, PaymentProcessorMock())
    assert "Can't pay an Order with total 0." in str(error_info.value)
 
