1class Solution(object):
2    def countPermutations(self, complexity):
3        """
4        :type complexity: List[int]
5        :rtype: int
6        """
7        n = len(complexity)
8        for i in range(1, n):
9            if complexity[i] <= complexity[0]:
10                return 0
11
12        ans, mod = 1, 10**9 + 7
13        for i in range(2, n):
14            ans = ans * i % mod
15        return ans