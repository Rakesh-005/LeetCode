1class Solution:
2    def minSubarray(self, nums: List[int], p: int) -> int:
3        ts=sum(nums)
4        r=ts%p
5        if r==0:
6            return 0
7        d={0:-1}
8        ps=0
9        ml=len(nums)
10        for i,n in enumerate(nums):
11            ps+=n
12            cm=ps%p
13            tm=(cm-r+p)%p
14            if tm in d:
15                ml=min(ml,i-d[tm])
16            d[cm]=i
17        return ml if ml<len(nums) else -1