c=0
n=int(input())
s=list(map(int,input().split()))
s_=list(filter(lambda i: i%2==0, s))
for i in s_:c+=1
print(c)