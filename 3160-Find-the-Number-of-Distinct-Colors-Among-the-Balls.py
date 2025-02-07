from typing import List

class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        d1 = {}  # Maps key b to value c
        d2 = {}  # Counts occurrences of each value in d1
        s = set()  # Keeps track of unique values in d1
        l = []

        for b, c in queries:
            if b in d1:
                p = d1[b]  # Previous value of b
                d2[p] -= 1
                if d2[p] == 0:  # Remove from set if count reaches zero
                    s.remove(p)

            d1[b] = c
            d2[c] = d2.get(c, 0) + 1
            s.add(c)
            l.append(len(s))  # Store count of unique values

        return l
