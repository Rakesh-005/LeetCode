class Solution(object):
    def maximumImportance(self, n, roads):
        \\\
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        \\\
        d=[0]*n
        for i in roads:
            d[i[0]]+=1
            d[i[1]]+=1
        d=sorted(d,reverse=True)
        res=0
        for i,j in enumerate(d):
            res+=(n-i)*j
        return res