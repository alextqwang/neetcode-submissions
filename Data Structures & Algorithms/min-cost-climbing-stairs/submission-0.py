class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        length = len(cost)
        d = {}
        d[0] = 0
        d[1] = 0
        for i in range(2, length + 1):
            d[i] = min(d[i - 2] + cost[i - 2], d[i - 1] + cost[i - 1])
        return d[length]