#leet code
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums)==1:
            if nums[0]==target:
                return 0
            else:
                return -1
        low=0
        high=len(nums)-1
        mid=0
        while low<=high:
            mid=(high+low)//2
            if nums[mid]>target:
                high=mid-1
            elif nums[mid]<target:
                low=mid+1
            else:
                return mid
        return -1
