class Solution:
    # think as linear representation of binary search. determine row, column by using simple math
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start = 0
        m = len(matrix)
        n = len(matrix[0])
        end = (m * n) - 1 # linear representation of last index

        
        while start <= end:
            mid = (end+start)//2
            i = mid//n # calculate row from linear represtation
            j = mid%n # calculate column from linear represtation
            # rest is normal as binary search
            if matrix[i][j] == target:
                return True
            if matrix[i][j] > target:
                end = mid - 1
            else:
                start = mid + 1
            
        return False
