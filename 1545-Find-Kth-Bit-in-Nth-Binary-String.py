class Solution(object):
    def findKthBit(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        def invert(s):
            y=''
            for i in s:
                y+='1' if i=='0' else '0'
            return y
        def a(n):
            if n==1:
                return '0'
            x=a(n-1)
            return x+'1'+invert(x)[::-1]
        return a(n)[k-1]