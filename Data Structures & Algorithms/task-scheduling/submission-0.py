class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        count = Counter(tasks)
        max_heap = []
        heapq.heapify(max_heap)

        for value in count.values():
            heapq.heappush(max_heap, -value)
        
        queue = deque()
        time = 0

        while max_heap or queue:
            time += 1

            if max_heap:
                val = 1 + heapq.heappop(max_heap)
                if val != 0:
                    queue.append((val, time + n))
            
            if queue and queue[0][1] == time:
                heapq.heappush(max_heap, queue.popleft()[0])
        
        return time
                

        

                



