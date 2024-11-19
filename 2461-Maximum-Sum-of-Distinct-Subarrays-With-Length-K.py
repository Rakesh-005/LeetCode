class Solution(object):
    def maximumSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        m=0
        s=set()
        j=0
        n=len(nums)
        su=0
        for i in range(n):
            while nums[i] in s:
                su-=nums[j]
                s.remove(nums[j])
                j+=1
            s.add(nums[i])
            su+=nums[i]
            if len(s)==k:
                m=max(m,su)
                su-=nums[j]
                s.remove(nums[j])
                j+=1
        return m