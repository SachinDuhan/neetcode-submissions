class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        
        # count = {}

        # for num in nums:
        #     count[num] = count.get(num, 0) + 1
        
        # sorted_pairs = sorted(count.items(), key = lambda x: x[1], reverse=True)

        # result = []

        # for i in range(k):
        #     result.append(sorted_pairs[i][0])
        
        # return result

        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
            
        freq_buckets = [[] for _ in range(len(nums) + 1)]
        
        for num, freq in count.items():
            freq_buckets[freq].append(num)
            
        result = []
        for i in range(len(freq_buckets) - 1, 0, -1):
            for num in freq_buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result