from pytest import raises
from pay.credit_card import CreditCard
from pay.processor import PaymentProcessor


API_KEY = "6cfb67f3-6281-4031-b893-ea85db0dce20"

def test_constructor():
    payment_processor = PaymentProcessor('')
    assert payment_processor.api_key == ''
    

def test_check_api_key_success():
    payment_processor = PaymentProcessor(API_KEY)
    valid_api_key = payment_processor.check_api_key()
    
    assert valid_api_key


def test_check_api_key_error():
    payment_processor = PaymentProcessor('invalid key')
    invalid_api_key = not payment_processor.check_api_key()
    
    assert invalid_api_key


def test_luhn_checksum_success():
    payment_processor = PaymentProcessor(API_KEY)
    sum_is_valid = payment_processor.luhn_checksum("1249190007575069")
    
    assert sum_is_valid


def test_luhn_checksum_error():
    payment_processor = PaymentProcessor(API_KEY)
    sum_is_not_valid = not payment_processor.luhn_checksum("11234567891012135")
    
    assert sum_is_not_valid


def test_validate_card_success():
    card = CreditCard(
        card_number="1249190007575069",
        month=12,
        year=2025,
        amount=100,
    )
    payment_processor = PaymentProcessor(API_KEY)
    card_is_valid = payment_processor.validate_card(card)
    
    assert card_is_valid


def test_validate_card_error():
    card = CreditCard(
        card_number="1249190007575069",
        month=12,
        year=1988,
        amount=100,
    )
    payment_processor = PaymentProcessor(API_KEY)
    card_is_not_valid = not payment_processor.validate_card(card)
    
    assert card_is_not_valid


def test_charge_success():
    credit_card = CreditCard(
        card_number="1249190007575069",
        month=12,
        year=2025,
        amount=100,
    )
    payment_processor = PaymentProcessor(API_KEY)
    payment_processor.charge(credit_card, 500)


def test_charge_card_error():
    credit_card = CreditCard(
        card_number="1249190007575069",
        month=12,
        year=1988,
        amount=100,
    )
    payment_processor = PaymentProcessor(API_KEY)
    
    with raises(ValueError) as error_info:
        payment_processor.charge(credit_card, 500)
    assert "Invalid card" in str(error_info.value)


def test_charge_api_error():
    credit_card = CreditCard(
        card_number="1249190007575069",
        month=12,
        year=1988,
        amount=100,
    )
    payment_processor = PaymentProcessor('invalid-key')
    
    with raises(ValueError) as error_info:
        payment_processor.charge(credit_card, 500)
    assert "Invalid API key" in str(error_info.value)
