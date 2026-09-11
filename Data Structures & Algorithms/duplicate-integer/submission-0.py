class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash = [[] for _ in range(10)]

        for i in range(len(nums)):
            x = nums[i]
            x_hash = nums[i] % 10

            if x in hash[x_hash]:
                return True
            
            hash[x_hash].append(nums[i])
        return False
        