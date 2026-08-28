class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        rotten = deque([])
        fresh, minutes = 0, 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    rotten.append((i,j))
        
        if fresh == 0:
            return 0

        if not rotten:
            return -1

        while rotten:
            n = len(rotten)
            for _ in range(n):
                i, j = rotten.popleft()

                for dr, dc in directions:
                    row, col = dr + i, dc +j
                    if (row in range(rows) and col in range(cols) 
                        and grid[row][col] == 1):
                        grid[row][col] = 2
                        fresh -= 1
                        rotten.append((row, col))

                if fresh == 0:
                    return minutes + 1
                
            minutes += 1

        if fresh > 0:
            return -1

        return minutes