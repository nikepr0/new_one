n=int(input())

def s(n):
    for i in range(n+1):
        if i%2==0:
            yield i
            
if n!=0 and n!=1:
    for i in s(n):
        if i%n!=0 and i!=n-1 or i==0:
            print(i ,end=",")
        else:
            print(i,end="")
else:
    print(0)