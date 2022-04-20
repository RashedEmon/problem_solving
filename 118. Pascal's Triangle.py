class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        ans = [[1], [1, 1]] #pre generate two rows of pascal triangle
        for i in range(2, numRows):
            temp = []
            temp.append(1) #we know that first value and last value of pascal triagle's row is 1. so i append 1 at first and last in the row.
            for j in range(1, i):
                temp.append(ans[i-1][j-1] + ans[i-1][j])  #from observation, we know that the value of a row element is the summation of two above value of previous row.
            temp.append(1) #we know that first value and last value of pascal triagle's row is 1. so I append 1 at first and last in the row.
            ans.append(temp)
        return ans
