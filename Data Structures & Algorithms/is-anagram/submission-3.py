class Solution:
    def hashfunc(self, s:str) -> int:
        sum_of_char = 0

        for ch in s:
            sum_of_char += ord(ch)
        
        return sum_of_char % 26

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        h1 = [0] * 26
        h2 = [0] * 26

        for i in range(len(s)):
            hash_s = self.hashfunc(s[i])
            hash_t = self.hashfunc(t[i])

            h1[hash_s]+=1
            h2[hash_t]+=1
        
        if h1 == h2:
            return True
        else:
            return False

        