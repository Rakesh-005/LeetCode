class Solution:
    def frequencySort(self, s: str) -> str:
        mh=[]
        res=''
        for i in set(s):
            heapq.heappush(mh,(-s.count(i),i))
        while mh:
            a,b=heapq.heappop(mh)
            res+=b*(-a)
        return res