"""Problem 308: 506939. Bank Account Class

Create a class Account with owner and balance. Add methods deposit and withdraw. Withdrawals should not be allowed if the amount exceeds the current balance.
Input format

An initial balance and a withdrawal amount .
Output format

The new balance after withdrawal, or the string ’Insufficient Funds’ if ."""
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        # в этой задаче deposit, похоже, не используется,
        # но метод должен быть
    
    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient Funds"
        else:
            self.balance -= amount
            return self.balance


# Чтение входных данных
B, W = map(int, input().split())

# Создаём объект с произвольным именем владельца
# (в условии имя не используется в выводе, поэтому любое)
acc = Account("User", B)

# Пытаемся снять деньги
result = acc.withdraw(W)

# Вывод результата
print(result)