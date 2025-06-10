class Solution:
    def maxDifference(self, s: str) -> int:
        c=Counter(s)
        return max([i for i in c.values() if i%2==1])-min([i for i in c.values() if i%2==0])
        