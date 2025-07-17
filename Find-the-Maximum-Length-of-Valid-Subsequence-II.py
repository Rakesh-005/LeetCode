class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:

        nums = [num % k for num in nums]
        n = len(nums)
        ma = 0
        for val in range(k):
            dp = [0]*k
            for num in nums:
                dp[num] = dp[val-num] + 1
            ma = max(ma,max(dp))
        return ma


        