# namespace UnitTest.Pay.Processor

import os
from datetime import datetime
from pay.credit_card import CreditCard
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY") or ""


class PaymentProcessor:
    def __init__(self, api_key: str) -> None:
        self.api_key = api_key

  
    def check_api_key(self) -> bool:
        return self.api_key == API_KEY


    def charge(self, credit_card: CreditCard, amount: int) -> None:
        if not self.check_api_key():
            raise ValueError("Invalid API key")
        if not self.validate_card(credit_card):
            raise ValueError("Invalid card")
        print(f"Charging card number {credit_card.card_number} for ${amount/100:.2f}")


    def validate_card(self, credit_card: CreditCard) -> bool:
        return luhn_checksum(credit_card.card_number) and datetime(credit_card.year, credit_card.month, 1) > datetime.now()


def luhn_checksum(card_number: str) -> bool:
    def digits_of(card_nr: str):
        return [int(d) for d in card_nr]
    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = 0
    checksum += sum(odd_digits)
    for digit in even_digits:
        checksum += sum(digits_of(str(digit * 2)))
    return checksum % 10 == 0
