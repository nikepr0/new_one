n=int(input())
s=list(map(int , input().split()))
ad=sorted(set(s))
for i in ad:
    print(i ,end=" ")