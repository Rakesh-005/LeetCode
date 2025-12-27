1class Solution:
2    def mostBooked(self, n: int, m: List[List[int]]) -> int:
3        r, c = [0]*n, [0]*n # rooms, counter
4        for s, e in sorted(m):
5            found = 0
6            for i,f in enumerate(r):
7                if f <= s:
8                    r[i] = e
9                    c[i] += 1
10                    found = 1
11                    break
12
13            if not found:
14                q = r.index(min(r))
15                r[q] += e-s
16                c[q] += 1
17
18        return c.index(max(c))