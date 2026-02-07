1class Solution(object):
2    def minimumDeletions(self, s):
3        """
4        :type s: str
5        :rtype: int
6        """
7        bc=0
8        mind=0
9        for i in s:
10            if i=='a':
11                mind=min(mind+1,bc)
12            else:
13                bc+=1
14        return mind