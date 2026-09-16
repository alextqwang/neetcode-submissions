class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 1
        j = len(numbers)
        curr = numbers[i - 1] + numbers[j - 1]
        while curr != target:
            if curr < target: 
                i += 1
            elif curr > target:
                j -= 1
            curr = numbers[i - 1] + numbers[j - 1]
        return [i, j]