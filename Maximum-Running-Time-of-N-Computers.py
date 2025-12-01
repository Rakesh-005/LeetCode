1class Solution:
2    def maxRunTime(self, n: int, arr: List[int]) -> int:
3        arr.sort()
4        total = sum(arr)
5
6        while arr[-1] > total // n:
7            n -= 1
8            total -= arr.pop()
9
10        return total // n
11