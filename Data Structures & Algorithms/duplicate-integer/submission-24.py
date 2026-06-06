class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        seen = set()

        for numbers in nums:
            if numbers not in seen:
                seen.add(numbers)
            else:
                return True
            
       
            
        return False
        

        