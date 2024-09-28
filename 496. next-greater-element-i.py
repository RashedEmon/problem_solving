class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        nums1_hashmap = {v:i for i, v in enumerate(nums1)}
        
        stack = []
        result = [-1 for _ in nums1]

        for i in range(len(nums2)):
            while stack and nums2[stack[-1]] < nums2[i]:
                idx = stack.pop()
                if nums2[idx] in nums1_hashmap:
                    result[nums1_hashmap[nums2[idx]]] = nums2[i]

            stack.append(i)
        return result
