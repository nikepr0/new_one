n=int(input())
def s():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b
    
dada=s()
for _ in range(n):
    if _!=n-1:
        print(next(dada), end=",")
    else:
        print(next(dada), end="")