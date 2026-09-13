class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        length = len(nums)
        d = {}
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        lists = [[] for _ in range(length + 1)]
        for num, count in d.items():
            lists[count].append(num)

        solution = []
        count = 0
        i = len(nums)
        while count < k:
            if lists[i]:
                for j in lists[i]:
                    solution.append(j)
                    count += 1
            i -= 1
        return solution