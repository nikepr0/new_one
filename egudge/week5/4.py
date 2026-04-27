import re
n=input()

s=re.findall('\d' ,n)

for i in s:
    print(i, end=" ")