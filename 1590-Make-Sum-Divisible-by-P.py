class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        ts=sum(nums)
        r=ts%p
        if r==0:
            return 0
        d={0:-1}
        ps=0
        ml=len(nums)
        for i,n in enumerate(nums):
            ps+=n
            cm=ps%p
            tm=(cm-r+p)%p
            if tm in d:
                ml=min(ml,i-d[tm])
            d[cm]=i
        return ml if ml<len(nums) else -1