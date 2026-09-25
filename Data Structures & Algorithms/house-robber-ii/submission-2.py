class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(numbers: List[int]) -> int:
            if len(numbers) == 1:
                return numbers[0]
            f0 = numbers[0]
            f1 = max(f0, numbers[1])
            for i in range(2, len(numbers)):
                temp = f0
                f0 = f1
                f1 = max(temp + numbers[i], f1)
            return f1
        
        if len(nums) == 1:
            return nums[0]
        return max(helper(nums[1:]), helper(nums[:-1]))