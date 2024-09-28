class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        '''
        Prepare a hashmap of nums1 where the key will be the value and the index will be the value of the hashmap.
        Initialize the result list with -1. Length of result list same as nums1.
        First, iterate through nums2 and push the number into the stack until it finds a number greater than the previous numbers.
        When it finds a greater number, it will start popping and check that the num is present in the nums1 using nums1_hashmap(number vs index mapping).
        If it finds in nums1 then it will get the index and replace the greater element into the index of the result list.
        '''
        nums1_hashmap = {num:index for index, num in enumerate(nums1)}
        
        stack = []
        result = [-1 for _ in nums1]

        for i in range(len(nums2)):
            while stack and nums2[stack[-1]] < nums2[i]:
                idx = stack.pop()
                if nums2[idx] in nums1_hashmap:
                    result[nums1_hashmap[nums2[idx]]] = nums2[i]

            stack.append(i)
        return result
