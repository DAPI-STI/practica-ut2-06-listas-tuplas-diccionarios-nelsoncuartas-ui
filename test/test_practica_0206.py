import pytest

from src.ex01_reverse_list import reverse_list
from src.ex02_unique_preserve_order import unique_preserve_order
from src.ex03_min_max_prices import min_max_prices
from src.ex04_best_student import best_student
from src.ex05_currency_symbol import currency_symbol
from src.ex06_checkout import checkout


# ---------------------------
# LISTAS
# ---------------------------

def test_ex01_reverse_list():
    data = [7, 3, 10, 1]
    out = reverse_list(data)
    assert out == [1, 10, 3, 7]
    assert data == [7, 3, 10, 1]  # original intacta
    assert reverse_list([]) == []


def test_ex02_unique_preserve_order():
    data = [3, 1, 3, 2, 1]
    out = unique_preserve_order(data)
    assert out == [3, 1, 2]
    assert data == [3, 1, 3, 2, 1]  # original intacta

    assert unique_preserve_order([]) == []
    assert unique_preserve_order([1, 1, 1]) == [1]
    assert unique_preserve_order([2, 1, 2, 3, 3, 2]) == [2, 1, 3]


# ---------------------------
# TUPLAS
# ---------------------------

def test_ex03_min_max_prices():
    assert min_max_prices([50, 75, 46, 22, 80, 65, 8]) == (8, 80)
    with pytest.raises(ValueError):
        min_max_prices([])


def test_ex04_best_student():
    records = [("Ana", 7.5), ("Luis", 9.0), ("Marta", 8.0)]
    assert best_student(records) == ("Luis", 9.0)

    # empate: devuelve el primero con esa nota
    records2 = [("A", 9.0), ("B", 9.0)]
    assert best_student(records2) == ("A", 9.0)

    with pytest.raises(ValueError):
        best_student([])


# ---------------------------
# DICCIONARIOS
# ---------------------------

def test_ex05_currency_symbol():
    assert currency_symbol("Euro") == "€"
    assert currency_symbol("Yen") == "¥"
    assert currency_symbol("Bitcoin") is None


def test_ex06_checkout():
    per_product, total = checkout([("Pan", 2), ("Huevos", 1), ("Pan", 1)])
    assert per_product == {"Pan": 4.2, "Huevos": 2.3}
    assert total == 6.5

    # carrito vacío
    per_product, total = checkout([])
    assert per_product == {}
    assert total == 0.0

    # unidades negativas
    with pytest.raises(ValueError):
        checkout([("Pan", -1)])

    # producto inexistente
    with pytest.raises(ValueError):
        checkout([("NoExiste", 1)])