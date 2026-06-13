class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-x for x in stones]

        heapq.heapify(max_heap)

        while max_heap:
            x = -heapq.heappop(max_heap)
            if not max_heap:
                return x

            y = -heapq.heappop(max_heap)

            diff = x - y
            if diff > 0:
                heapq.heappush(max_heap, -diff)

        return 0