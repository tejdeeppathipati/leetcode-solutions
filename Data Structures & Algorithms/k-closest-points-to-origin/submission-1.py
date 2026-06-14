class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        result = []
        heapq.heapify(max_heap)

        for arr in points:
            dist = (arr[0] * arr[0]) + (arr[1] * arr[1])
            if len(max_heap) < k:
                heapq.heappush(max_heap, (-dist, arr))
            else:
                top = heapq.heappop(max_heap)
                if -top[0] > dist:
                    heapq.heappush(max_heap, (-dist, arr))
                else:
                    heapq.heappush(max_heap, (top[0], top[1]))
        
        for heap in max_heap:
            result.append(heap[1])

        return result
