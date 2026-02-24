"""Problem 309: 506942. Circle Area

Define a Circle class that takes a radius. Implement an area method. Use .
Input format

An integer .
Output format

The area of the circle formatted to 2 decimal places."""
class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        pi = 3.14159
        return pi * self.radius * self.radius


# Чтение входных данных
r = int(input().strip())

# Создаём объект класса Circle
circle = Circle(r)

# Вычисляем площадь
area_value = circle.area()

# Выводим ровно с двумя знаками после точки
print(f"{area_value:.2f}")