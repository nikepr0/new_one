import re 
d=list(input())
r=re.compile(r'\d{1}')
for i in range(len(d)):
    f=r.findall(d[i])
    if f:
        d[i]=d[i]*2
for j in d:
    print(j,end="")