class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        indegree = [0] * numCourses
        # [1,0], [2, 1], [3, 2], [4, 1], [5, 4], [2, 5]
        # indegree = [0, 1, 2, 1, 1, 1]

        adj = [[] for i in range(numCourses)]
        for crs, prereq in prerequisites:
            indegree[crs] += 1
            # adjacency list 
            adj[prereq].append(crs)

        
        q = deque()
        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)
        # queue = [0]
        finish = 0
        while q:
            node = q.popleft()
            finish += 1
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        return finish == numCourses