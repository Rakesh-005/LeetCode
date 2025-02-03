class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        x=1
        m=0
        y=len(nums)-1
        for i in range(y):
            if nums[i]>nums[i+1]:
                x+=1
            else:
                m=max(m,x)
                x=1
        m=max(m,x)
        x=1
        for i in range(y):
            if nums[i]<nums[i+1]:
                x+=1
            else:
                m=max(m,x)
                x=1
        return max(m,x)