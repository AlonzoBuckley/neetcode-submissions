class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        for i, val in enumerate(nums):
            difference = target - val
            if difference in visited:
                return [visited[difference],i]
            visited[val] = i
        return
            
        