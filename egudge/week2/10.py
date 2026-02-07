a=int(input())
nums=list(map(int,input().split()))
for i in range(a):
    for j in range(a):
        if nums[i]>nums[j]:
            nums[i],nums[j]=nums[j],nums[i]
            
print(*nums)            
