class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ms=m=nums[0]
        for i in nums[1:]:
            ms=max(i,ms+i)
            m=max(m,ms)
        return m