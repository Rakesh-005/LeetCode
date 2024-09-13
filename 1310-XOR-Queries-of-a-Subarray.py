class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n=len(arr)
        p=[0]*(n+1)
        for i in range(1,n+1):
            p[i]=p[i-1]^arr[i-1]
        ans=[]
        for l,r in queries:
            ans.append(p[l]^p[r+1])
        return ans