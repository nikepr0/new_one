"""Define a class Person with:

    A constructor that takes name and stores it as an attribute

Define a child class Student that inherits from Person with:

    A constructor that takes name and gpa, calls the parent constructor using super(), and stores gpa as an additional attribute

    A display() method that prints the student’s information in the format: Student: [name], GPA: [gpa]

Input format

A string and a float .
Output format

The string: Student: [name], GPA: [gpa]"""
class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):
    def __init__(self, name, gpa):
        super().__init__(name)
        self.gpa = gpa
    
    def display(self):
        print(f"Student: {self.name}, GPA: {self.gpa}")


# Чтение входных данных
name, gpa_str = input().split()
gpa = float(gpa_str)

# Создание объекта студента
student = Student(name, gpa)

# Вывод информации
student.display()