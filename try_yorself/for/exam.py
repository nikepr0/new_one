n=int(input())
lst=list(map(int, input().split()))

for i in lst:
    if i%2==0 and i%3==0:
        print(i, end=" ")