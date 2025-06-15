import heapq

class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        l = []
        for idx, row in enumerate(mat):
            heapq.heappush(l, (-row.count(1), idx))
        count_neg, idx = heapq.heappop(l)
        return [idx, -count_neg]
