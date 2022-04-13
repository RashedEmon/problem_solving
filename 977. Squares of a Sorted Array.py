class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        arr = [item*item for item in nums]
        arr.sort()
        return arr
