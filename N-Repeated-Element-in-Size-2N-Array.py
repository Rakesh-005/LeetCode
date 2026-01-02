1class Solution(object):
2    def repeatedNTimes(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: int
6        """
7        for i in nums:
8            if nums.count(i)>1:
9                return i