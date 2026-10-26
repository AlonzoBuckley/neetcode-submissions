class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited_nums = {} # value : index

        for i, num in enumerate(nums):
            diff = target - num #number needed to reach target
            if diff in visited_nums: #diff in hashmap
                return [visited_nums[diff], i] #obtain indicies
            visited_nums[num] = i #diff not in hashmap so we add num to hasmap, could be used later
        
        return #failed to find any indicies that reach target
        