class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #without division, we can just iterate over the entire list (left and right of num) 
        # n times, one for each number and multiply
        # That is O(n^2)... better would be to keep track of a running product
        length = len(nums)
        solution = [1] * length
        product = 1
        for i, num in enumerate(nums):
            solution[i] *= product
            product *= num
        # That is the running product, meaning everything is multiplied by everything to the
        # left except itself, so we have to do the right now
        product = 1
        for j in range(length - 1, -1, -1):
            solution[j] *= product
            product *= nums[j]
        return solution
        
