"""Problem 311: 506945. Pair Addition

Define a Pair class with two integer values ( and ). Create a method add that takes another Pair object and returns their sum.
Input format

Four integers .
Output format

The sum in the format: Result: [a_sum] [b_sum]"""
class Pair:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def add(self, other):
        return Pair(self.a + other.a, self.b + other.b)


# Чтение четырёх чисел с одной строки
a1, b1, a2, b2 = map(int, input().split())

# Создаём два объекта Pair
p1 = Pair(a1, b1)
p2 = Pair(a2, b2)

# Складываем их
result = p1.add(p2)

# Вывод в требуемом формате
print(f"Result: {result.a} {result.b}")