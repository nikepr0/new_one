import re
n=input()
r=re.compile('\d+')
s=r.fullmatch(n)

print("Match" if s else "No match")