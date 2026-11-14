class Solution(object):
    def minimumSumSubarray(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: int
        :type r: int
        :rtype: int
        """
        n=len(nums)
        pref=[0]*(n+1)
        for i in range(n):
            pref[i+1]=pref[i]+nums[i]

        best=float('inf')
        for length in range(l,r+1):
            for i in range(n-length+1):
                s=pref[i+length]-pref[i]
                if 0<s<best:
                    best=s
        return -1 if best==float('inf') else best 