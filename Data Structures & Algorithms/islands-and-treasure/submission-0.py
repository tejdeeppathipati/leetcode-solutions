class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        '''
        [[2147483647,-1,0,1],
        [2147483647,2147483647,1,-1],
        [2147483647,-1,2147483647,-1],
        [0,-1,2147483647,2147483647]]
        '''
        queue = deque()
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    queue.append((i, j))

        while queue:
            row, col = queue.popleft()

            for dr, dc in directions:
                nr = row + dr
                nc = col + dc

                if (0 <= nr < ROWS and 0 <= nc < COLS 
                    and grid[nr][nc] == 2147483647):

                    newVal = grid[row][col] + 1
                    grid[nr][nc] = min(grid[nr][nc], newVal)
                    queue.append((nr, nc))
    