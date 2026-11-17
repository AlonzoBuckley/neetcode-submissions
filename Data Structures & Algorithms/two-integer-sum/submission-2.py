class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited_nums = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in visited_nums:
                return [visited_nums[diff], i]
            visited_nums[num] = i
        