n = int(input())

prime = True

for i in range(3, n):
    if n % i == 0:
        prime = False

if prime:
    print("Yes")
else:
    print("No")