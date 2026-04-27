import re
n=input()

f=re.findall(r'\w+' , n)
print(len(f))