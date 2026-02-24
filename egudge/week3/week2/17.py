n = int(input())
num = {}

for i in range(n):
    s = input()
    if s not in num:
        num[s] = 1
    else:
        num[s] += 1

count = 0
for i in num:
    if num[i] == 3:
        count += 1
        


print(count)