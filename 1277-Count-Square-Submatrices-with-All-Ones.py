class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        n,m=len(matrix),len(matrix[0])
        ans=0
        for i in range(n):
            ans+=matrix[i][0]
        for j in range(1,m):
            ans+=matrix[0][j]
        for i in range(1,n):
            for j in range(1,m):
                if matrix[i][j]==1:
                    matrix[i][j]=1+min(matrix[i-1][j],matrix[i][j-1],matrix[i-1][j-1])
                ans+=matrix[i][j]
        return ans