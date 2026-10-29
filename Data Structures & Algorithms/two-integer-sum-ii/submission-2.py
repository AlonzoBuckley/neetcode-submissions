class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #pointers at start and end of our array
        l = 0
        r = len(numbers) - 1

        while l < r: #left pointer will always be less than right pointer
            curr_sum = numbers[l] + numbers[r] # current value of pointers

            if curr_sum < target: 
                l += 1 #increment left pointer
            elif curr_sum > target:
                r -= 1 #decrement right pointer
            else:
                
                return [l + 1, r + 1] #found target with these indicies, add 1 because 1-indexed
        
        