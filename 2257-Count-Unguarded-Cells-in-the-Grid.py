class Solution(object):
    def dfs(self,r,c,dir,vis,mp):
        n=len(vis)
        m=len(vis[0])
        if (r,c) in mp:
            return
        if r<0 or c<0 or r>=n or c>=m:
            return
        vis[r][c]=1
        if dir=='r':
            self.dfs(r,c+1,'r',vis,mp)
        elif dir=='l':
            self.dfs(r,c-1,'l',vis,mp)
        elif dir=='d':
            self.dfs(r+1,c,'d',vis,mp)
        else:
            self.dfs(r-1,c,'u',vis,mp)
        
        
    def countUnguarded(self, m, n, guards, walls):
        """
        :type m: int
        :type n: int
        :type guards: List[List[int]]
        :type walls: List[List[int]]
        :rtype: int
        """
        mp={}
        vis=[[0]*n for _ in range(m)]
        for x,y in guards:
            mp[(x,y)]=1
            vis[x][y]=1
        for x,y in walls:
            mp[(x,y)]=1
            vis[x][y]=1
        for x,y in guards:
            self.dfs(x,y+1,'r',vis,mp)
            self.dfs(x,y-1,'l',vis,mp)
            self.dfs(x+1,y,'d',vis,mp)
            self.dfs(x-1,y,'u',vis,mp)
        return sum(vis[i][j]==0 for i in range(m) for j in range(n))