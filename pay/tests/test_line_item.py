from pay.order import LineItem


def test_line_item():
    line_item = LineItem('Test Default', 100)
    assert line_item.total == 100


def test_line_item_wth_quantity():
    line_item = LineItem('Test With Quantity', 200, 5)
    assert line_item.total == 1000
