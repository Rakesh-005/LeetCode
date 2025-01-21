class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n=len(grid[0])
        ls=sum(grid[0])
        rs=0
        res=float('inf')
        for i in range(n):
            ls-=grid[0][i]
            res=min(res,max(ls,rs))
            rs+=grid[1][i]
        return res