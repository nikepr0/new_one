a=int(input())
list=input().split()
s=0 
last=a-1 ; mas=int(list[0]) ; pos=0

for i in range(0 , a):
    if int(list[i])>mas:
        mas=int(list[i])
        pos=i
print(pos+1)
