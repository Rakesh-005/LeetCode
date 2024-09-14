class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ans=0
        cnt=0
        m=max(nums)
        for i in nums:
            if i==m:
                cnt+=1
            else:
                cnt=0
            ans=max(ans,cnt)
        return ans