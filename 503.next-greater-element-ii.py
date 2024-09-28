class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        '''
        # Using Monotonic Stack
        Intialize a result list with -1 same length of nums list.
        Iterate through the nums list twice, to simulate circular motion we use modulo.
        It will only push index to stack for first cycle of iterations.
        For first cycle it will calculate next greater element for most of the item and some item may be uncalulated.
        For those items it will go for second cycle.
        '''
        n = len(nums)
        result = [-1 for num in nums]
        stack = []

        for i in range(2*n):
            current_index = i % n
            while stack and nums[stack[-1]] < nums[current_index]:
                result[stack.pop()] = nums[current_index]
            if i < n:
                stack.append(current_index)
        
        return result
