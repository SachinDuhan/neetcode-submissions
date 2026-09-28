class Solution:
    def isPalindrome(self, s: str) -> bool:

        st = ""

        for ch in s:
            if ord(ch) in range(65,91) or ord(ch) in range(97,123) or ch.isdigit():
                st+=ch

        for i in range(len(st)//2):
            if st[i].lower() == st[len(st)-i-1].lower():
                print(st[i])
                pass
            else:
                return False
        return True
        