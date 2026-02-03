a=int(input())
nums=[a]
for i in range(1,a):
    nums.append(int(input()))
for i in range(a):
    for j in range(a):
        if nums[i]>nums[j]:
            nums[i],nums[j]=nums[j],nums[i]
            # swap completed
            
for i in range(a):
    nums[i]=nums[a-1-i]
print(*nums)