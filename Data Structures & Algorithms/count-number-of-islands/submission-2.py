class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        islands = 0

        def recursive_dfs(row, col):
            if (row < 0 or row >= rows 
                or col < 0 or col >= cols
                or grid[row][col] != "1"):

                return 

            grid[row][col] = "0"
            recursive_dfs(row + 1, col)
            recursive_dfs(row - 1, col)
            recursive_dfs(row, col + 1)
            recursive_dfs(row, col - 1)


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    recursive_dfs(i, j)
                    islands += 1
        
        return islands

