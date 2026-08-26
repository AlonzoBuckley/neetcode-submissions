class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        no_dublicates = set(nums)
        
        if sorted(list(no_dublicates)) == sorted(nums):
            return False
        else:
            return True
            
        