class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=0
        r=len(nums)-3
        op=0
        while l<=r:
            if nums[l] == 0:
                for i in range(l, l + 3):
                    nums[i] = 1 - nums[i]
                op += 1
            l += 1
        return op if nums==[1]*len(nums) else -1