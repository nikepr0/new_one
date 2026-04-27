n=input()
a=list(n)
def s(a):
    a.reverse()
    for i in a:
        yield i
            

for i in s(a):
    print(i,end="")