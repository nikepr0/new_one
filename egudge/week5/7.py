import re 
n=input()
d=input()
s=input()

res=re.sub(d , s , n)
print(res)