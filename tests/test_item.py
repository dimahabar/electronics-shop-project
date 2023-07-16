import pytest
from src.item import Item

"""Здесь надо написать тесты с использованием pytest для модуля item."""
def test_item_all():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)
    assert len(Item.all) == 2

def test_calculate_total_price():
    assert 100 * 20 == 2000

def test_apply_discount():
    Item.pay_rate = 0.5
    assert 100 * Item.pay_rate == 50