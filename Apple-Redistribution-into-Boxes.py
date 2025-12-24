1class Solution:
2    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
3        total_apples = sum(apple)
4        capacity.sort(reverse=True)
5
6        need = 0
7        while total_apples > 0:
8            total_apples -= capacity[need]
9            need += 1
10
11        return need