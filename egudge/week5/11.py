import re 
f=0
n=input().split()

for i in n:
    for j in i:
        if re.match(r'[A-Z]',j):
            f+=1
print(f)