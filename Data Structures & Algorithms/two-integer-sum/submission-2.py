class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        blank = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    blank.append(i)
                    blank.append(j)
                    return blank
                else:
                    pass
        