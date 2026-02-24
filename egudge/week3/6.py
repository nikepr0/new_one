"""Problem 306: 506935. Rectangle Subclass

Create a class Rectangle that inherits from Shape. It should take length and width as arguments. Override the area method to return .
Input format

Two integers: and .
Output format

The area of the rectangle."""
# Предполагаемый базовый класс (для локального тестирования)
class Shape:
    def area(self):
        pass  # будет переопределён в дочерних классах


# Решение задачи
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width


# Чтение входных данных и вывод результата
length, width = map(int, input().split())

rect = Rectangle(length, width)
print(rect.area())