a=int(input())
lise=input().split()

if a==0:
    print()
else:
    mx=max(lise)
    mn=min(lise)

for i in range(a):
    if lise[i]==mx:
        lise[i]=mn

print(*lise)