class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        result = []
        heapq.heapify(max_heap)

        for arr in points:
            dist = (arr[0] ** 2) + (arr[1] * arr[1])
            heapq.heappush(max_heap, (-dist, arr))

            if len(max_heap) > k:
                heapq.heappop(max_heap)
        
        for heap in max_heap:
            result.append(heap[1])

        return result
