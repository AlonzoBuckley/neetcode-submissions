class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        no_dups = set(nums)
        return sorted(nums) != sorted(list(no_dups))
        