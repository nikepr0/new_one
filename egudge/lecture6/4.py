n=int(input())
s=map(int , input().split())
f=map(int , input().split())
d=[0]
for j, i in zip(s,f):
    d.append(j*i)
print(sum(d))