class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = []
        for char in s:
            if char.isalpha() or char.isnumeric():
                new_s.append(char.lower())
               
        if new_s == new_s[::-1]: #start, stop, step
            return True
        else: 
            return False

        