class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        sorted_nums=nums
        sorted_nums.sort()
        for i in range(0,len(nums),2):
            if sorted_nums[i]!=sorted_nums[i+1]:
                return False
        return True