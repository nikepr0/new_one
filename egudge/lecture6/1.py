import re
n=int(input())
s=list(map(int,input().split()))
s_=list(map(lambda i: i**2, s))
print(sum(s_))
