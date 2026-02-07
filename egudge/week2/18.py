n = int(input())
num = {}

for i in range(n):
    s = input()
    if s not in num:
        num[s] = i + 1

num = dict(sorted(num.items()))

for i in num:
    print(i, num[i])