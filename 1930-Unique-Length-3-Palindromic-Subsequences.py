class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        c=0
        for e in set(s):
            i,j=s.find(e),s.rfind(e)
            c+=len(set(s[i+1:j]))
        return c