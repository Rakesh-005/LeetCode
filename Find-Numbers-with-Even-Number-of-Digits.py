class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s=0
        for i in nums:
            if len(str(i))%2==0:
                s+=1
        return s