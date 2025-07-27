class Solution:
    def coinChange(self,coins, amount):
        # Initialize DP array with 'inf', except for dp[0] = 0
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        # Build the dp array
        for a in range(1, amount + 1):
            for coin in coins:
                if a - coin >= 0:
                    dp[a] = min(dp[a], dp[a - coin] + 1)

        # If amount can't be formed, return -1
        return dp[amount] if dp[amount] != float('inf') else -1
