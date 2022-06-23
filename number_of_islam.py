#number of connected element #dfs
class Solution:
    def solve(self, i:int, j:int, grid: List[List[str]],visited: List[List[bool]]):
        
        if i < 0 or j < 0 or i >= len(grid) or j>= len(grid[0]) or grid[i][j] == "0":
            return
        if visited[i][j]:
            return
        else:
            visited[i][j] = True
        
        self.solve(i+1,j,grid,visited)
        self.solve(i,j+1,grid,visited)
        self.solve(i-1,j,grid,visited)
        self.solve(i,j-1,grid,visited)
        
    def numIslands(self, grid: List[List[str]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        
        visited = [[False for i in range(n)] for j in range(m)]
        
        count = 0
        
        for i in range(m):
            for j in range(n):
                if visited[i][j] == False and grid[i][j] == "1":
                    self.solve(i,j,grid,visited)
                    #print(visited)
                    count+=1
        return count
        
    
