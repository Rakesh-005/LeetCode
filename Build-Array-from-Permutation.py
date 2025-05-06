class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        l=[0]*len(nums)
        for i in nums:
            l[i]=nums[nums[i]]
        return l