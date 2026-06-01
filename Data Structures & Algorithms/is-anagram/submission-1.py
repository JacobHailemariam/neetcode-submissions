class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_List = sorted(list(s))
        t_List = sorted(list(t))
        if s_List == t_List:
            return True
        return False
        
        