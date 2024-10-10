class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
        Here I have used two pointer concept. 
        It will iterate through the list once. when find same element then it will increase pointer by one and replace the element pointer is pointing with current value up to 2 times.
        if we find non equal adjacent element then reset to counter value 1 and increase pointer by one and replace pointer pointing value by current element.
        At last return pointer + 1.
        '''
        pointer = 0
        counter = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                counter = 1
                pointer += 1
                nums[pointer] = nums[i]
            else:
                counter += 1
                if counter <= 2:
                    pointer += 1
                    nums[pointer] = nums[i]

        return pointer+1
