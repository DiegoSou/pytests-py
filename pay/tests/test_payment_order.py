from pytest import raises, MonkeyPatch
from pay.payment import pay_order
from pay.order import Order, LineItem
from pay.processor import PaymentProcessor


def test_pay_order_success(monkeypatch: MonkeyPatch):
    # mock input data using monkeypatch
    inputs = [
        "0", # card number
        "0", # month
        "0" # year
    ]
    monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))
    monkeypatch.setattr(PaymentProcessor, "check_api_key", lambda _: True)
    monkeypatch.setattr(PaymentProcessor, "charge", lambda self, card, month, year, amount: None)
    line_items = [LineItem('Test Line Item', 100, 5)]
    order = Order(line_items)
    pay_order(order)


def test_pay_order_error():
    line_items = []
    order = Order(line_items)
    with raises(ValueError) as error_info:
        pay_order(order)
    assert "Can't pay an Order with total 0." in str(error_info.value)
 
