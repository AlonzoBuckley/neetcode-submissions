class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = "" # empty string 
        for c in s: # loop through every char in our given string
            if c.isalnum(): # if alphanumeric
                new_s += c.lower() # add char to our new string
        return new_s == new_s[::-1] #check if palindrome
        