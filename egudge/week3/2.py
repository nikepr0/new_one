"""Problem 302: 194007. Is a Number Usual?

You’re given a single integer number n, and you need to determine whether this number is usual or not. We call the number usual if the prime 
factors of this number are limited to 2, 3 and 5. If the given number is usual, print Yes; otherwise, print No.

Important: Solve the problem by implementing a function:

bool isUsual(int num)
Input format

Integer number n .
Output format

Print Yes if the number is usual; otherwise, print No"""


def is_usual(num: int) -> bool:
    if num <= 0:
        return False
    
    # Делим на 2 сколько можно
    while num % 2 == 0:
        num //= 2
    
    # Делим на 3 сколько можно
    while num % 3 == 0:
        num //= 3
    
    # Делим на 5 сколько можно
    while num % 5 == 0:
        num //= 5
    
    # Если осталось 1 — значит число было вида 2^a × 3^b × 5^c
    return num == 1
# Основная программа
n = int(input().strip())

if is_usual(n):
    print("Yes")
else:
    print("No")