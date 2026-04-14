from coffee_shop.menu import MenuItem, Menu


def test_menu_item_creation():
    item = MenuItem("Espresso", 2.50, "drink")
    assert item.name == "Espresso"
    assert item.base_price == 2.50
    assert item.category == "drink"


def test_menu_item_negative_price():
    import pytest
    with pytest.raises(ValueError, match="negative"):
        MenuItem("Bad", -1.0, "drink")


def test_menu_add_and_get():
    menu = Menu()
    menu.add(MenuItem("Latte", 4.50, "drink"))
    assert "Latte" in menu
    assert menu.get("Latte").base_price == 4.50


def test_menu_get_missing():
    menu = Menu()
    assert menu.get("Ghost") is None
