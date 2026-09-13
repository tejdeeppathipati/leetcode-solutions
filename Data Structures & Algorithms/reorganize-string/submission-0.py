class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        max_heap = []

        for char, cnt in count.items():
            max_heap.append((-cnt, char))
        
        heapq.heapify(max_heap)
        prev = None
        output = ""

        while max_heap or prev:
            if not max_heap and prev:
                return ""
            
            cnt, char = heapq.heappop(max_heap)
            output += char
            cnt += 1
            
            if prev:
                heapq.heappush(max_heap, prev)
                prev = None

            if cnt:
                prev = (cnt, char)

        return output


            

        