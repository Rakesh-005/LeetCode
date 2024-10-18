class Solution:
    def b(self,nums,ind,cu,m,c):
        if cu==m:
            c[0]+=1
        for i in range(ind,len(nums)):
            self.b(nums,i+1,cu|nums[i],m,c)
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        m=0
        for i in nums:
            m|=i
        c=[0]
        self.b(nums,0,0,m,c)
        return c[0]