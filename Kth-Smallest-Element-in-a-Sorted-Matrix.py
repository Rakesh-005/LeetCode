import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        l=[]
        for i in matrix:
            for j in i:
                heapq.heappush(l,-(j))
                if len(l)>k:
                    heapq.heappop(l)
        return -heapq.heappop(l)