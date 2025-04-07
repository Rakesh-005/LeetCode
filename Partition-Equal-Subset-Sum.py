from collections import defaultdict

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2
        dp = defaultdict(int)
        dp[0] = 1

        for num in nums:
            current = dict(dp)  # copy current state
            for s in current:
                dp[s + num] += current[s]


        return dp[target] > 0  # We only care if there's at least one way
