
class Solution:
    def isPalindrome(self, s: str) -> bool:
        empt = []
        for c in s:
            if c.isalnum():
                empt.append(c.lower())
        return empt == empt[::-1]
    


    