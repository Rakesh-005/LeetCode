class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        l=[0]*(n)
        for s,e in edges:
            l[e]+=1
        c=0
        ans=0
        for i in range(n):
            if l[i]==0:
                c+=1
                ans=i
        if c>1:
            return -1
        return ans