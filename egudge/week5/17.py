import re 
n=input()

s=re.findall(r'\d{2}/\d{2}/\d{4}',n)

print(len(s))