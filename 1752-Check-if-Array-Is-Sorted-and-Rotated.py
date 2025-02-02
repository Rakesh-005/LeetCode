class Solution(object):
    def check(self, nums):
        if sorted(nums) == nums:
            return True
            
        for i in range(len(nums)):
            nums.append(nums.pop(0))
            if nums == sorted(nums):
                return True
        return False
        