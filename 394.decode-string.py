#
# @lc app=leetcode id=394 lang=python3
#
# [394] Decode String
#

# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        n = len(s)
        repetitions = 0
        i = 0
        while i < n:
            while s[i].isdigit():
                repetitions += int(s[i])
                if s[i+1].isdigit():#Will IndexError at malformed input
                    repetitions *= 10
                i += 1
            
            if s[i] == "[":
                stack.append(repetitions)
                repetitions = 0
            elif s[i] == "]":
                #Backtrack until we get to the number 
                chars = []
                #print(stack)
                while stack and type(stack[-1]) == str:
                    chars.append(stack.pop())
                reps = stack.pop()
                stack.append(reps * "".join(chars[::-1]))
            else:
                stack.append(s[i])
            i += 1
        
        return "".join(stack) 
                
                    
                
                

            
        
# @lc code=end

