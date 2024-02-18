from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter1 = Counter(nums1)
        counter2 = Counter(nums2)
        result = []

        if len(counter1) > len(counter2):
            temp = counter1
            counter1 =  counter2
            counter2 = temp
        
        for key, count in counter1.items():
            if key in counter2:
                result.extend([key for _ in range(min(count, counter2[key]))])
        return result
