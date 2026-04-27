import re
n=input()
s=input()

m=re.search(s,n)
if m:
    print("Yes")
else:
    print("No")