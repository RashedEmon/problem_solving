# Store those rows and columns containing 0 in two separate lists. one for rows and another for columns.
# Then iterate through rows and make all the row elements into 0.
# Then iterate through columns and make all the column elements into 0.

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = set()
        columns = set()

        for row in range(len(matrix)):
            for column in range(len(matrix[0])):
                if matrix[row][column] == 0:
                    if row not in rows:
                        rows.add(row)
                    if column not in columns:
                        columns.add(column)
        
        for row in rows:
            for i in range(len(matrix[0])): 
                matrix[row][i] = 0
        
        for i in range(len(matrix)): 
            for column in columns:
                matrix[i][column] = 0
        
