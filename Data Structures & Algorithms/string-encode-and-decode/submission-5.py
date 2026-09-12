class Solution:

    def encode(self, strs: List[str]) -> str:
        # return "#@#fuck#@#" if len(strs) == 0 else "!#!".join(strs)
        result = ""
        for s in strs:
            result += str(len(s))
            result += "#"
            result += s
        print(result)
        return result

    def decode(self, s: str) -> List[str]:
        # return [] if s == "#@#fuck#@#" else s.split("!#!") 

        result = []
        pointer = 0

        while pointer < len(s):
            n = ""
            word = ""

            while s[pointer] != "#":
                n += s[pointer]
                pointer+=1
            
            pointer += 1

            for i in range(int(n)):
                word += s[pointer]
                pointer += 1
            
            print(word)
            
            result.append(word)
            
            # pointer += 1
        return result
