from collections import defaultdict
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        D=defaultdict(list)

        for i in arr:
            D[bin(i).count('1')].append(i)

        return [i for k in sorted(D.keys()) for i in sorted(D[k])]