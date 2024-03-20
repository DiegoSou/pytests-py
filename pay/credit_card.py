# namespace UnitTest.Pay.CreditCard

from dataclasses import dataclass

@dataclass
class CreditCard:
    card_number: str
    month: int
    year: int
    amount: int
