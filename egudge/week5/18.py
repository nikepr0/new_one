import re
n=input()
s=input()

es=re.escape(s)
print(es, end=' '  )
print(len(re.findall(es, n)))