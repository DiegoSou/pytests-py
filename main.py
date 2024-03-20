# namespace UnitTest.Main

from pay.order import LineItem, Order
from pay.payment import pay_order

def main():
    order = Order()
    order.line_items.append(LineItem(name="Shoes", price=100_00, quantity=2))
    order.line_items.append(LineItem(name="Hat", price=50_00))
    
    card_number = input("Please enter your card number: ") # ex: 1249190007575069
    month = int(input("Please enter the card expiry month: "))
    year = int(input("Please enter the card expiry year: "))
    
    pay_order(order)

if __name__ == "__main__":
    main()
