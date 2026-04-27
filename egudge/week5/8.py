import re
s=input()
d=input()

res=re.split(d,s)
print(res)

for i in range(len(res)):
    if i!=len(res)-1:
        print(res[i]+",",end="") 
    else:
        print(res[i])