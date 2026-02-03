a=int(input()) 
d=0
lis_t=map(int , input().split())
for i in lis_t:
    if i>0:
        d+=1
print(d)