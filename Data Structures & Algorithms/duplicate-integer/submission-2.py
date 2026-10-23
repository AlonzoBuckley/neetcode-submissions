class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        noduplicate = set(nums)
        if sorted(nums) == sorted(list(noduplicate)):
            return False
        else:
            return True