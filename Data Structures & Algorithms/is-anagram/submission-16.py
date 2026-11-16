class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #base case return false if length is different
        if len(s) != len(t):
            return False
        
        #creating s counter
        counter = {}   
        for char in s:
            counter[char] = counter.get(char,0) + 1
        
        #trying to eliminate each number count to 0 relying on T

        for char in t:
            if char not in counter:
                return False
            counter[char] -= 1
            
        if list(counter.values()) == [0] * len(list(counter.values())):
            return True
        return False