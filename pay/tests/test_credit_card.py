from pay.credit_card import CreditCard


def test_attributest():
    card = CreditCard(
        card_number="1249190007575069",
        month=12,
        year=2025,
        amount=100,
    )
    assert card.card_number == "1249190007575069"
    assert card.month == 12
    assert card.year == 2025
    assert card.amount == 100
