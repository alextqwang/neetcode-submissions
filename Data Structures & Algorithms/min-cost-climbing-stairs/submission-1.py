class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        length = len(cost)
        f0 = 0
        f1 = 0
        for i in range(2, length + 1):
            temp = f0
            f0 = f1
            f1 = min(cost[i - 1] + f1, cost[i - 2] + temp)
        return f1