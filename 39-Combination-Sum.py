class Solution(object):
    def combinationSum(self, c, t):
        \\\
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        \\\
        def b(s,t,p):
            if t==0:
                l.append(p)
                return
            if t<0:
                return
            for i in range(s,len(c)):
                b(i,t-c[i],p+[c[i]])
        l=[]
        c.sort()
        b(0,t,[])
        return l