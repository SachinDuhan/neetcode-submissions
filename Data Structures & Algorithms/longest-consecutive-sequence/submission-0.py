class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # s = defaultdict(list)

        # num = set(nums)


        # for n in num:
        #     if n -1 not in num:
        #         s[n].append(n)
        #     else :
        #         s[n-1].append(n)
        
        # print(s)

        # for k,v in s.items():
        #     if v[-1] in s.keys():
        #         s[k].extend(s[v[-1]])
        # print(s)

        nums = set(nums)

        current = 0

        longest = 0

        for n in nums:
            if n-1 not in nums:
                current = 1

                while (n+current) in nums:
                    current += 1
                
                longest = max(longest, current)

        return longest
            