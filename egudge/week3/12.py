class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary
    
    def total_salary(self):
        return self.base_salary


class Manager(Employee):
    def __init__(self, name, base_salary, bonus_percent):
        super().__init__(name, base_salary)
        self.bonus_percent = bonus_percent
    
    def total_salary(self):
        return self.base_salary * (1 + self.bonus_percent / 100)


class Developer(Employee):
    def __init__(self, name, base_salary, completed_projects):
        super().__init__(name, base_salary)
        self.completed_projects = completed_projects
    
    def total_salary(self):
        return self.base_salary + self.completed_projects * 500


class Intern(Employee):
    def __init__(self, name, base_salary):
        super().__init__(name, base_salary)
    
    # total_salary уже наследуется от Employee — просто base_salary


# Чтение входной строки
line = input().strip().split()

role = line[0]
name = line[1]
base_salary = int(line[2])

if role == "Manager":
    bonus_percent = int(line[3])
    emp = Manager(name, base_salary, bonus_percent)
elif role == "Developer":
    projects = int(line[3])
    emp = Developer(name, base_salary, projects)
elif role == "Intern":
    emp = Intern(name, base_salary)
else:
    # В реальном контесте обычно вход гарантированно корректен
    emp = Employee(name, base_salary)

# Вывод результата с двумя знаками после точки
total = emp.total_salary()
print(f"Name: {emp.name}, Total: {total:.2f}")