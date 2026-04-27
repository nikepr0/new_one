a,d=map(int, input().split())

def s(a,d):
    for i in range(a,d+1):
        yield i*i
        
for i in s(a,d):
    print(i)