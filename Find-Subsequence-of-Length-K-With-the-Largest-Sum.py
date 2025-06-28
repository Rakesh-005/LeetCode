class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        minHeap = []
        ans = []
        for a in nums:
            if len(minHeap) < k:
                heappush(minHeap , a)
                ans.append(a)
            else:
                if a > minHeap[0]:
                    z = heappop(minHeap)
                    ans.remove(z)
                    heappush(minHeap , a)
                    ans.append(a)
        return ans