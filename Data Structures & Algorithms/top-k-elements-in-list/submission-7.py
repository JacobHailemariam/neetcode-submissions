class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}

        buckets = [[] for _ in range(len(nums) + 1)]
        
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        
        for number, count in counter.items():
            buckets[count].append(number)
        


        result = []
        for i in range(len(buckets) - 1, 0 ,-1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result
        
