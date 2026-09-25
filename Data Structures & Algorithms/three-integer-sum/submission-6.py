class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        sort = sorted(nums)
        firsts = sort[:(length - 2)]
        solution = []
        for i, num in enumerate(firsts):
            if i > 0:
                if num == firsts[i - 1]:
                    continue
            target = 0 - num
            p1 = i + 1
            p2 = length - 1
            while p1 < p2:
                current = sort[p1] + sort[p2]
                if current == target:
                    solution.append([num, sort[p1], sort[p2]])
                    while p1 < p2 and sort[p1] == sort[p1 + 1]:
                        p1 += 1
                    while p1 < p2 and sort[p2] == sort[p2 - 1]:
                        p2 -= 1
                    p1 += 1
                    p2 -= 1
                elif current < target:
                    p1 += 1
                else:
                    p2 -= 1

        return solution