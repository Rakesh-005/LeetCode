class Solution(object):
    def rotateTheBox(self, box):
        """
        :type box: List[List[str]]
        :rtype: List[List[str]]
        """
        m,n=len(box),len(box[0])
        ans=[['.']*m for _ in range(n)]
        for i,row in enumerate(box):
            b=n-1
            for j in range(n-1,-1,-1):
                if row[j]=='#':
                    ans[b][m-i-1]='#'
                    b-=1
                elif row[j]=='*':
                    ans[j][m-i-1]='*'
                    b=j-1
        return ans