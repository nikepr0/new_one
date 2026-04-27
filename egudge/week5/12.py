import re
n=input()

d=re.findall(r'\d{2,}' , n)

for i in d:
    print(i, end=" ")