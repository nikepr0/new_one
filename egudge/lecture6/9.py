first=int(input())
second=input().split()
third=input().split()
four=input().strip()
dic1=dict(zip(second , third))

if four in dic1:
    print(dic1[four])
else:
    print("Not found")