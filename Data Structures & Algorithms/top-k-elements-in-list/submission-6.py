class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        n = len(nums)
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        buckets = [[] for _ in range(n + 1)]
        for key in d:
            buckets[d[key]].append(key)
        count = 0
        solution = []
        l = len(nums)
        while count < k:
            if buckets[l]:
                for i in buckets[l]:
                    solution.append(i)
                    count += 1
            l -= 1
        return solution