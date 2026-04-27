c=int(input())

def s(c):
    for i in range(c+1):
        yield 2**i
        
for i in s(c):
    print(i,  end=" ") 