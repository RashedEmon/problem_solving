# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        if n==1:
            if isBadVersion(n):
                return n
            
        low=1
        high=n
        
        while low <= high:
            mid=low+(high-low)//2
            if not isBadVersion(mid):
                low=mid+1
            else:
                high=mid-1
        
        if isBadVersion(low):
            return low
        else:
            return low+1
