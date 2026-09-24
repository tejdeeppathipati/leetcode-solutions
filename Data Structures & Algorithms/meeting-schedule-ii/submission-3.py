"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        # 0, 5, 15
        # 10, 20, 40
        result, inUse = 0, 0
        s, e = 0, 0 

        while s < len(start):
            if start[s] < end[e]:
                s += 1
                inUse += 1
            else:
                e += 1
                inUse -= 1
            
            result = max(result, inUse)
        
        return result

