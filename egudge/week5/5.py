import re 
n=input()

s=re.match(r'^\D+\d$',n)
if s:
    print("Yes")
else:
    print("No")