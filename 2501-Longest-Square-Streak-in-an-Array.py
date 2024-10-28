class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()
        d={}
        res=-1
        for i in nums:
            if i**0.5 in d:
                d[i]=d[i**0.5]+1
                res=max(res,d[i])
            else:
                d[i]=1
        return res