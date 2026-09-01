class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        pac_seen, atl_seen = set(), set()
        pac_queue, atl_queue = deque(), deque()

        for col in range(n):
            pac_seen.add((0, col))
            pac_queue.append((0, col))

            atl_seen.add((m-1, col))
            atl_queue.append((m - 1, col))
        
        for row in range(1, m):
            pac_seen.add((row, 0))
            pac_queue.append((row, 0))

        for row in range(0, m-1):
            atl_seen.add((row, n-1))
            atl_queue.append((row, n-1))
        
        def bfs(queue, seen):
            while queue:
                row, col = queue.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (0 <= nr < m and 0 <= nc < n
                        and (nr, nc) not in seen
                        and heights[nr][nc] >= heights[row][col]):

                        seen.add((nr, nc))
                        queue.append((nr, nc))
        
        bfs(pac_queue, pac_seen)
        bfs(atl_queue, atl_seen)

        return list(pac_seen & atl_seen)


