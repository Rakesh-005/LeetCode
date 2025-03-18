class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        left, bitMask, maxi = 0, 0, 0
        n = len(nums)
        
        for right in range(n):
            while (bitMask & nums[right]) != 0:
                bitMask -= nums[left]
                left += 1
            bitMask += nums[right]
            maxi = max(maxi, right - left + 1)
        
        return maxi