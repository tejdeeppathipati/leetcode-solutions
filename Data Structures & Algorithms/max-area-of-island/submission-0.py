class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        seen = set()  
        output = 0
        directions = ((-1, 0), (1, 0), (0, 1), (0, -1))
        row, col = len(grid), len(grid[0])

        def dfs(i, j):
            grid[i][j] = 0
            area = 1
            for dr, dc in directions:
                nr, nc = i + dr, j + dc
                if ((0 <= nr < row) 
                    and (0 <= nc < col) 
                    and (grid[nr][nc] == 1)):
                    area += dfs(nr, nc)

            return area
            
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    output = max(output, dfs(i, j))

        return output
