"""Problem 307: 506936. Point Coordinates

Create a Point class that stores and coordinates. Implement the following methods:

    show() — prints coordinates in the format (x, y)

    move(new_x, new_y) — changes the point’s coordinates to the new values

    dist(other_point) — returns the Euclidean distance to another point

Your program should create a point, show its initial coordinates, move it to a new position, show the updated coordinates, create a second point, and print the distance between the moved point and the second point.
Input format

Three lines, each containing two integers:

    Line 1: — initial coordinates of the point

    Line 2: — new coordinates to move the point to

    Line 3: — coordinates of the second point for distance calculation

Output format

Three lines:

    Line 1: Initial coordinates in (x, y) format

    Line 2: Coordinates after move() in (x, y) format

    Line 3: Euclidean distance to the second point, formatted to 2 decimal places
"""
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def show(self):
        print(f"({self.x}, {self.y})")
    
    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
    
    def dist(self, other_point):
        dx = self.x - other_point.x
        dy = self.y - other_point.y
        return math.sqrt(dx*dx + dy*dy)


# Чтение входных данных
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

# Создаём первую точку
p1 = Point(x1, y1)

# Показываем начальные координаты
p1.show()

# Перемещаем точку
p1.move(x2, y2)

# Показываем новые координаты
p1.show()

# Создаём вторую точку
p2 = Point(x3, y3)

# Вычисляем и выводим расстояние с двумя знаками после запятой
distance = p1.dist(p2)
print(f"{distance:.2f}")