class Solution(object):
    def check(self, nums):
        a=sorted(nums)
        if a == nums:
            return True
            
        for i in range(len(nums)):
            nums.append(nums.pop(0))
            if nums == a:
                return True
        return False
        