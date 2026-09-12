class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 2:
            return min(cost[0], cost[1])
        
        prev = cost[0] 
        curr = cost[1]

        for c in cost[2:]:
            prev, curr = curr, c + min(prev, curr)

        return min(prev, curr)