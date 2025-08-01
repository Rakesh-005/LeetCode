class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows==0:
            return []
        if numRows==1:
            return [[1]]
        up=self.generate(numRows-1)
        dn=[1]*numRows
        for i in range(1,numRows-1):
            dn[i]=up[-1][i-1]+up[-1][i]
        up.append(dn)
        return up
        