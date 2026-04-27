import re 
m=input()
paa=re.compile('\w+\s*')
s=len(paa.findall(m))
print(s)