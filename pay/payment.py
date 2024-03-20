# namespace UnitTest.Pay.Payment

from typing import Protocol
from pay.order import Order
from pay.credit_card import CreditCard


class PaymentProcessor(Protocol):
    def charge(self, card: CreditCard, amount: int):
        """Charges the card with passed amount"""
        

def pay_order(order: Order, credit_card: CreditCard, payment_processor: PaymentProcessor):
    if (order.total == 0):
        raise ValueError("Can't pay an Order with total 0.")
    payment_processor.charge(credit_card, amount=order.total)  
    order.pay()
