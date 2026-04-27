import re
n=input()
s=input()

d=re.findall(s,n)
print(len(d))