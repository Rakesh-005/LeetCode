class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d=Counter(nums)
        heap=[]
        for i,j in d.items():
            heapq.heappush(heap,(j,i))
            if len(heap)>k:
                heapq.heappop(heap)
        l=[]
        for i,j in heap:
            l.append(j)
        return l[::-1]