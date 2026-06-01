class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_List = sorted(s)
        t_List = sorted(t)
        if s_List == t_List:
            return True
        return False
        
        