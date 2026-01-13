"""
Archivo principal del proyecto.

Desde aquí puedes probar las funciones SIN usar pytest.
Este archivo NO se evalúa automáticamente.
"""

from .ex01_reverse_list import reverse_list
from .ex02_unique_preserve_order import unique_preserve_order
from .ex03_min_max_prices import min_max_prices
from .ex04_best_student import best_student
from .ex05_currency_symbol import currency_symbol
from .ex06_checkout import checkout


def main() -> None:
    print("=== Pruebas manuales ===")

    data = [7, 3, 10, 1]
    print("reverse_list([7,3,10,1]) ->", reverse_list(data))

    data2 = [3, 1, 3, 2, 1]
    print("unique_preserve_order([3,1,3,2,1]) ->", unique_preserve_order(data2))

    prices = [50, 75, 46, 22, 80, 65, 8]
    print("min_max_prices(prices) ->", min_max_prices(prices))

    records = [("Ana", 7.5), ("Luis", 9.0), ("Marta", 8.0)]
    print("best_student(records) ->", best_student(records))

    print("currency_symbol('Euro') ->", currency_symbol("Euro"))
    print("currency_symbol('Bitcoin') ->", currency_symbol("Bitcoin"))

    cart = [("Pan", 2), ("Huevos", 1), ("Pan", 1)]
    per_product, total = checkout(cart)
    print("checkout(cart) ->", per_product, total)


if __name__ == "__main__":
    main()
