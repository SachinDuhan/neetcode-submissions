class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}

        for i,v in enumerate(numbers):
            x = target - v

            if x in seen:
                return [seen[x]+1, i+1]
            
            seen[v] = i