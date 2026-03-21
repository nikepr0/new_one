# map_filter_reduce.py
# Примеры map, filter, reduce — классические встроенные функции

from functools import reduce


# ─── map ────────────────────────────────────────────────
def square(x):
    return x * x

numbers = [1, 2, 3, 4, 5, 6]

squared = list(map(square, numbers))
print("map → квадраты:", squared)                    # [1, 4, 9, 16, 25, 36]

# с lambda (чаще всего так и пишут)
squared2 = list(map(lambda x: x**2, numbers))
print("map + lambda  :", squared2)

# превратить числа в строки
str_nums = list(map(str, numbers))
print("в строки       :", str_nums)


# ─── filter ─────────────────────────────────────────────
def is_even(n):
    return n % 2 == 0

evens = list(filter(is_even, numbers))
print("\nfilter → чётные :", evens)                  # [2, 4, 6]

# с lambda
big_numbers = list(filter(lambda x: x > 3, numbers))
print("filter > 3      :", big_numbers)              # [4, 5, 6]


# ─── reduce ─────────────────────────────────────────────
# сумма всех элементов
total = reduce(lambda a, b: a + b, numbers)
print("\nreduce → сумма  :", total)                  # 21

# максимум
maximum = reduce(lambda a, b: a if a > b else b, numbers)
print("reduce → максимум:", maximum)                 # 6

# произведение
product = reduce(lambda a, b: a * b, numbers, 1)     # начальное значение 1 важно!
print("reduce → произведение:", product)             # 720


# ─── реальный пример: обработка списка заказов ──────────
orders = [
    {"item": "кофе",   "price": 890,  "qty": 2},
    {"item": "круассан","price": 450, "qty": 3},
    {"item": "чай",    "price": 300,  "qty": 1},
]

# общая сумма заказа
total_order = reduce(
    lambda acc, order: acc + order["price"] * order["qty"],
    orders,
    0
)
print("\nОбщая сумма заказа:", total_order, "₸")     # 3050 ₸