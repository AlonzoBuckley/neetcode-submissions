class Solution:
    def isValid(self, s: str) -> bool:
        arr = [""] #if closing bracket first prevent index out of range
        for c in s: # iterate through every character
            if c == "[" or c == "(" or c == "{": # open brackets
                arr.append(c) # add to list
            
            elif c == "]": #type of closing bracket
                if arr[-1] == "[": #check if back of array is corresponding opening bracket
                    arr.pop() #remove it from our arr
                else:
                    return False #not valid parentheses
        #repeat for other type of parentheses
            elif c == ")":
                if arr[-1] == "(":
                    arr.pop()
                else:
                    return False

            elif c == "}":
                if arr[-1] == "{":
                    arr.pop()
                else:
                    return False

        if len(arr) > 1: #if there is any content leftover in the arr
            return False
        
        
        return True
                
                

        