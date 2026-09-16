class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        setnums = set(nums)
        best = 1
        for i in setnums:
            if i - 1 not in setnums:
                curr = i
                count = 1
                while curr + 1 in setnums:
                    count += 1
                    curr += 1
                if count > best:
                    best = count
        return best