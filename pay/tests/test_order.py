from pay.order import Order, LineItem, OrderStatus


def test_order():
    order = Order()
   
    assert order.status == OrderStatus.OPEN
    assert order.line_items is not None
    assert len(order.line_items) == 0


def test_order_payment():
    order = Order()
    order.pay()
    
    assert order.status == OrderStatus.PAID


def test_order_total():
    order = Order([
        LineItem('First Line Item', 100, 5),
        LineItem('Second Line Item', 50, 10)
    ])
    
    assert order.total == 1000
