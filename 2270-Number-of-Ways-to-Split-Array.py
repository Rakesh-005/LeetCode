class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        c = 0 
        total_sum = sum(nums) 
        ls = 0 
        
        for i in range(len(nums) - 1):
            ls += nums[i]  
            rs = total_sum - ls 
            if ls >= rs:
                c += 1
        
        return c
