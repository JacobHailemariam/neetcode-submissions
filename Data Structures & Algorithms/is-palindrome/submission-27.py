def reverse(lst: list) -> list:
        reversed_lst = []
        for i in range(len(lst)-1,-1,-1):
            reversed_lst.append(lst[i])
        return reversed_lst

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [c.lower() for c in list(s) if c.isalnum()]
        return s == reverse(s)


    