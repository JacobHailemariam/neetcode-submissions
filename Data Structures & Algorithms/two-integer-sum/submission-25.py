class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {}
    
        for index,value in enumerate(nums):
            complement = target - value

            if complement in values:
                return [values[complement], index]
            
            values[value] = index
        
            