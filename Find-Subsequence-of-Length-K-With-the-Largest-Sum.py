class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        dup=sorted(nums)
        for i in range(len(nums)-k): 
            nums.remove(dup[i])
        return nums