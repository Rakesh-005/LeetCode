class Solution(object):
    def decrypt(self, code, k):
        """
        :type code: List[int]
        :type k: int
        :rtype: List[int]
        """
        n=len(code)
        if k==0:
            return [0]*n
        l=code+code
        for i in range(n):
            if k>0:
                code[i]=sum(l[i+1:i+k+1])
            else:
                code[i]=sum(l[n+k+i:n+i])
        return code
