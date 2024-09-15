class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        d={'a':1,'e':2,'i':4,'o':8,'u':16}
        f={0:-1}
        mask=0
        l=0
        for i,c in enumerate(s):
            if c in d:
                mask^=d[c]
            if mask in f:
                l=max(l,i-f[mask])
            else:
                f[mask]=i
        return l