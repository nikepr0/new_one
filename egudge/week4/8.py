s=int(input())

def prime(s):
    for i in range(2,s+1):
        for j in range(1,i):
            if i%j==0 and j!=1 and j!=i:
                break
        else:
            yield i 
            
for i in prime(s):
    print(i,end=" ")