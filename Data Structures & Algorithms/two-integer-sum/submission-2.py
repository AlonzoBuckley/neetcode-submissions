class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_indicies = {}
        for i, num in enumerate(nums):
            difference = target - num
            if difference in sum_indicies:
                return [sum_indicies[difference], i]
            sum_indicies[num] = i