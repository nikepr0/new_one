import re

n = input().strip()

if re.search(r'(cat|dog)', n):
    print("Yes")
else:
    print("No")