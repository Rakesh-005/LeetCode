class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        mh=[]
        for i in range(len(arr)-1):
            heapq.heappush(mh,(arr[i]/arr[-1],(i,len(arr)-1)))
        for i in range(k-1):
            i,j=heapq.heappop(mh)[1]
            if j-1>i:
                heapq.heappush(mh,(arr[i]/arr[j-1],(i,j-1)))
        a,b=heapq.heappop(mh)[1] 
        return [arr[a],arr[b]]