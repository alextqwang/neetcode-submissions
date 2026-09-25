class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 1:
            return nums[0]
        f0 = nums[0]
        f1 = max(f0, nums[1])
        for i in range(2, length):
            temp = f0
            f0 = f1
            f1 = max(temp + nums[i], f1)
        return f1
        