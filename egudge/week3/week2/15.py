n = int(input())

surnames = set()

for i in range(n):
    surnames.add(input().strip())

print(len(surnames))