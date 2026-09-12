import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        sufix = [1] * n
        result = [0] * n

        high = n-2
        low = 1

        prefix[1] = nums[0]

        sufix[high] = nums[n-1]

        while high > -1 and low < n-1:
            low += 1
            high -= 1
            # if low == 1:
            #     prefix[1] = nums[0]
            
            # if high == n-2:
            #     sufix[high] = nums[n-1]
            
            prefix[low] = nums[low-1] * prefix[low-1]
            sufix[high] = nums[high+1] * sufix[high+1]
            # result[low] = prefix[low] * sufix[low]
        # print(prefix)
        # print(sufix)
        for i in range(n):
            result[i] = prefix[i] * sufix[i]

        return result

