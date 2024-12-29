class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        c=nums[0]
        m=nums[0]
        for i in nums[1:]:
            c=max(i,c+i)
            m=max(m,c)
        return m