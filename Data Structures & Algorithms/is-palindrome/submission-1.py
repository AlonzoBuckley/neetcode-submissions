class Solution:
    def isPalindrome(self, s: str) -> bool:
        reverse_s = ""
        for char in s:
            if char.isalnum():
                reverse_s += char.lower()
        return reverse_s == reverse_s[::-1]
                

        