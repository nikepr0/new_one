import re 
n=input()

name=r'(\w+),'
age=re.compile(r'\s+\d+\b')

namee=re.search(name,n)
agee=age.search(n)

for i in namee.groups():
    print(i,end="")
    break
print(agee.group())