#leet code
def searchInsert(nums: List[int], target: int) -> int:
        low=0
        high=len(nums)-1
        mid=0
        
        while low <= high:
            mid = low+(high-low)//2
            if nums[mid] > target:
                high=mid-1
            elif nums[mid] < target:
                low=mid+1
            else:
                return mid
        return high+1
