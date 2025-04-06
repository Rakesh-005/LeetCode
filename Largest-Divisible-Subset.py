class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        dp=[[num] for num in nums]
        ms=dp[0]
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i]%nums[j]==0 and len(dp[j])+1>len(dp[i]):
                    dp[i]=dp[j]+[nums[i]]
                    if len(dp[i])>len(ms):
                        ms=dp[i]
        return ms
