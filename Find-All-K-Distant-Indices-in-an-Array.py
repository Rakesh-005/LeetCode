class Solution(object):
    def findKDistantIndices(self, nums, key, k):
        """
        :type nums: List[int]
        :type key: int
        :type k: int
        :rtype: List[int]
        """
        l1=[]
        for i,j in enumerate(nums):
            if j==key:
                l1.append(i)
        l2=[]
        for i in range(len(nums)):
            for j in l1:
                if abs(i-j)<=k:
                    l2.append(i)
                    break
        return sorted(l2)