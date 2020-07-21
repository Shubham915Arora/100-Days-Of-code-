class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l=s.strip().split(" ")
        a=len(l[-1])
        return a
    