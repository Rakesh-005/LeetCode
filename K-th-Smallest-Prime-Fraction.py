class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        mh=[]
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                heapq.heappush(mh,(arr[i]/arr[j],(arr[i],arr[j])))
        for i in range(k):
            a,b=heapq.heappop(mh)[1]
        return [a,b]