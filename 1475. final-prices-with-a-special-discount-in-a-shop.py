class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        '''
        Copy all elements in result list.
        Iterate through the prices list and push the index of the number into the stack. 
        When it find lesser number than previous numbers then it will start popping the stack until the top of the stack is greater or equal than the number.
        So, the popped index holding number will be greater than the number. Then it will use the index and replace the index containing value by the number.
        '''
        stack = []
        result = prices[:]

        for i in range(len(prices)):
            while stack and prices[stack[-1]] >= prices[i]:
                index = stack.pop()
                result[index] = prices[index] - prices[i]

            stack.append(i)
        return result

