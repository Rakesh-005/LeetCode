class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        p=0
        mip=0
        maxp=0
        for i in nums:
            p+=i
            mip=min(mip,p)
            maxp=max(maxp,p)
        return maxp-mip