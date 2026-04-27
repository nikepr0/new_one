import re
n=input().split()
da=False

for i in n:
    if re.search(r'\w+\@\D+\.\w+', i):
        da=True
        global s;s=i
        break
        
print(s if da else "No email")