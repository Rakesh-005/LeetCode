class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mp=0
        pri=prices[0]
        for i in range(1,len(prices)):
            p=prices[i]-pri
            if prices[i]<pri:
                pri=prices[i]
            elif mp<prices[i]-pri:
                mp=prices[i]-pri
        return mp