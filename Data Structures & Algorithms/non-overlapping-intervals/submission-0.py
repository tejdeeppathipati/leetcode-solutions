class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 1:
            return 0

        removed = 0
        intervals.sort()
        prev = intervals[0][1]

        for i in range(1, len(intervals)):
            if prev > intervals[i][0]:
                prev = min(prev, intervals[i][1])
                removed += 1
            else:
                prev = intervals[i][1]

        return removed 

