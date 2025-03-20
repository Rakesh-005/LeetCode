class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        par=[i for i in range(n)]
        bit_ands={i:-1 for i in range(n)}

        def find(x):
            while par[x]!=par[par[x]]: par[x]=par[par[x]]
            return par[x]
        
        def union(x,y,weight):
            px,py=find(x),find(y)
            par[py]=px
            bit_ands[px]=bit_ands[py]=(bit_ands[px] & bit_ands[py]) & weight
        
        for u,v,w in edges:
            union(u,v,w)
        
        ans=[]
        for x,y in query:
            if find(x)!=find(y): ans.append(-1)
            else: ans.append(bit_ands[par[x]])

        return ans