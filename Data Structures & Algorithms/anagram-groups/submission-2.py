from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # anagram_map = defaultdict(list)
        
        # for s in strs:
        #     sorted_key = "".join(sorted(s))
            
        #     anagram_map[sorted_key].append(s)
            
        # return list(anagram_map.values())

        anagram_map = defaultdict(list)

        for ch in strs:
            kkey = [0] * 26

            for c in ch:
                kkey[ord(c) - ord('a')] += 1
            
            anagram_map[tuple(kkey)].append(ch)
        return list(anagram_map.values())