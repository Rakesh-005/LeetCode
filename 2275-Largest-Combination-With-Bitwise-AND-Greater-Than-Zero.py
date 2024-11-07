class Solution(object):
    def largestCombination(self, candidates):
        """
        :type candidates: List[int]
        :rtype: int
        """
        a=0
        for i in range(32):
            cn=sum(1 for c in candidates if c&(1<<i))
            a=max(a,cn)
        return a