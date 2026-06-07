class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)

        empty = []
        for i in range(len(nums)):
            left = i+1 
            right = len(nums)-1
            while left < right:
                if nums[left]+ nums[right] +nums[i]== 0:
                    if [nums[i], nums[left], nums[right]] not in empty:
                        empty.append([nums[i],nums[left],nums[right]])
                    left+=1
                    right-=1
                elif nums[left]+nums[right]+nums[i] < 0:
                    left+=1
                else:
                    right-=1
        return empty
                            
                                
                        
        