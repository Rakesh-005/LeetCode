class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l=[]
        for i in arr:
            d=abs(i-x)
            heapq.heappush(l,(-d,-i))
            if len(l)>k:
                heapq.heappop(l)
        res=[-heapq.heappop(l)[1] for _ in range(k)]
        return sorted(res)