a=int(input())
nums=list(map(int,input().split()))

for i in range(a):
    nums[i]=nums[i]**2

print(*nums)