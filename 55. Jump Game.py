#dp bottom up solution
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        dp = [False for i in range(0,len(nums))]
        length = len(nums)
        targetIndex = length-1
        
        for i in range(length-1,-1,-1):
            if i+nums[i] >= targetIndex:
                dp[i]=True
                targetIndex = i
        return dp[0]
