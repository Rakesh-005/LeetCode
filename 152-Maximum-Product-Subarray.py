class Solution:
    def maxProduct(self, l: List[int]) -> int:
        a=l[0]
        b=l[0]
        c=l[0]
        for i in range(1,len(l)):
            ta=max(l[i],a*l[i],b*l[i])
            b=min(l[i],a*l[i],b*l[i])
            a=ta
            c=max(c,a)
        return c