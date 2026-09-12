class Solution:

    def encode(self, strs: List[str]) -> str:
        return "#@#fuck#@#" if len(strs) == 0 else "!#!".join(strs)

    def decode(self, s: str) -> List[str]:
        return [] if s == "#@#fuck#@#" else s.split("!#!") 
