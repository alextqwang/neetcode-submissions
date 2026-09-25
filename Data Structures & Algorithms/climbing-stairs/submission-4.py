class Solution:
    def climbStairs(self, n: int) -> int:
        f0 = 0
        f1 = 1
        i = 1
        while i < n:
            tracker = f0
            f0 = f1
            f1 += tracker
            i += 1
        return f0 + f1