class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp_list = []
        prev = -1
        for i in range(len(nums)-1, -1, -1):
            if nums[i] >= prev:
                prev = nums[i]
                temp_list.append(nums[i])
            else:
                idx = self.immediate_senior(nums[i], temp_list)
                nums[i], temp_list[idx] = temp_list[idx], nums[i]
                for temp in temp_list:
                    i+=1
                    nums[i] = temp
                return
            
        for i, temp in enumerate(temp_list):
            nums[i] = temp

    def immediate_senior(self, num, num_list):
        for i, n in enumerate(num_list):
            if n > num:
                return i
            
