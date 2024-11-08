class Solution(object):
    def getMaximumXor(self, nums, maximumBit):
        """
        :type nums: List[int]
        :type maximumBit: int
        :rtype: List[int]
        """
        n=len(nums)
        pre=[]
        mask=(1<<maximumBit)-1
        for x in nums:
            pre.append(mask^x)
            mask=mask^x
        pre.reverse()
        return pre