class Solution(object):
    def countSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        m=max(nums)
        l=0
        n=len(nums)
        f=0
        t=0
        for r in range(n):
            if nums[r]==m:
                f+=1
            while f>=k:
                t+=n-r
                if nums[l]==m:
                    f-=1
                l+=1
        return t