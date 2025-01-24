class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        l=[]
        for i in range(len(arr)):
            for j in range(i,len(arr)):
                l.append([arr[i],arr[j]])
        l.sort(key=lambda x: x[0]/x[1])
        return l[k-1]
        
        