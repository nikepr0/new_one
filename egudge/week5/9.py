import re 
n=input()

s=re.split(r'\s+', n)
count=0

for i in range(len(s)):
    if len(s[i])==3:
        count+=1
        
print(count)