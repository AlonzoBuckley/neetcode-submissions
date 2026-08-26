class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}
        for char in s:
            if char not in s_dict:
                s_dict[char] = 1 #initial add to dict
            else:
                s_dict[char] +=1 #update that character was found again
        #repeat for t
        for char in t:
            if char not in t_dict:
                t_dict[char] = 1 
            else:
                t_dict[char] +=1 
        #compare them
        if s_dict == t_dict:
            return True
        else:
            return False #not anagram

        