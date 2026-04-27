a=int(input())

def s(a):
    while a>=0:
        yield a
        a-=1
        
for i in s(a):
    print(i)