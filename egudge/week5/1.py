import re
n=input()

m=re.match("Hello",n)
if m:
    print("Yes")
else:
    print("No")