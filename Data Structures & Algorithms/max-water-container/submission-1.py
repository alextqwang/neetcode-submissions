class Solution:
    def maxArea(self, heights: List[int]) -> int:
        p1 = 0
        p2 = len(heights) - 1
        width = p2 - p1
        best = width * min(heights[p1], heights[p2])
        while p1 < p2:
            if heights[p1] < heights[p2]:
                while p1 < p2 and heights[p1] >= heights[p1 + 1]:
                    p1 += 1
                p1 += 1
            elif heights[p1] > heights[p2]:
                while p1 < p2 and heights[p2] >= heights[p2 - 1]:
                    p2 -= 1
                p2 -= 1
            else:
                p1 += 1
            width = p2 - p1
            best = max(best, width * min(heights[p1], heights[p2]))
        return best