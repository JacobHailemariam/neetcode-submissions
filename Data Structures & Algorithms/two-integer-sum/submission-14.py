class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for indice,value in enumerate(nums):
            ## 0,   3   DIFF IS 4    {key 3: 0, 4:}
            diff = target - value

            if diff in nums_dict:
                return [nums_dict[diff],indice]
            else:
                nums_dict[value] = indice