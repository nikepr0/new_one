n=input().split()
a=list(n)
s=int(input())

def d(a,s):
    b=a*s
    for i in b:
        yield i
    
for i in d(a,s):
    print(i, end=" ")