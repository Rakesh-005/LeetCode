class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        d={}
        m=-1
        for i in nums:
            s=sum(int(j) for j in str(i))
            if s not in d:
                d[s]=i
            else:
                m=max(m,i+d[s])
                d[s]=max(d[s],i)
        return m