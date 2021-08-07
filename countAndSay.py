# leetcode medium

class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        prev = self.countAndSay(n-1)
        i = 0
        returnstr = ''
        
        while i < len(prev):
            digit = prev[i]
            count = 1
            
            i += 1
            
            while i < len(prev) and prev[i] == digit:
                count += 1
                i += 1
                
            returnstr += str(count) + digit
                
                
            
        return returnstr
            
            
