nums=[0,0,1]
end=len(nums)-1
start=0
while start < end:
    if nums[start]==0:
        nums.pop(start)
        nums.append(0)
        start-=1
        end-=1
    start+=1
print(nums)
