class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}

        buckets = [[] for _ in range(len(nums) + 1) ]

        for num in nums:
            counter[num] = counter.get(num, 0) + 1

        for number, count in counter.items():
            #drop the number into the bucket
            buckets[count].append(number)
        

        result = []
        for count in range(len(buckets) - 1, 0, -1):
            for i in buckets[count]:
                result.append(i)
                if len(result) == k:
                    return result
        



