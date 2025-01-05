
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l=[]
        for i in set(nums):
            if nums.count(i)>math.ceil(len(nums)//3):
                l.append(i)
        return l