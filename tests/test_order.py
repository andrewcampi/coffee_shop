import pytest
from coffee_shop.order import Order, OrderItem


def test_order_item_count():
    order = Order("Alice")
    order.add_item(OrderItem("Latte", quantity=2))
    order.add_item(OrderItem("Croissant", quantity=1))
    assert order.item_count() == 3


def test_order_is_empty():
    order = Order("Bob")
    assert order.is_empty()
    order.add_item(OrderItem("Espresso"))
    assert not order.is_empty()


def test_order_item_invalid_quantity():
    with pytest.raises(ValueError, match="at least 1"):
        OrderItem("Latte", quantity=0)
