class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [c for c in s.lower() if c.isalnum()]
        reverse = []
        for i in range(len(s)-1,-1,-1):
            reverse.append(s[i])
        return s == reverse