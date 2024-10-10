class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        m=0
        l=[]
        for i in range(len(nums)):
            if not l or nums[l[-1]]>nums[i]:
                l.append(i)
        for i in range(len(nums)-1,0,-1):
            while l and nums[l[-1]]<=nums[i]:
                m=max(m,i-l[-1])
                l.pop() 
        return m