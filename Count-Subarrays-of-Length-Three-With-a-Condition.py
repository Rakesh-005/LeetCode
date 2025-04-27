class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        c=0
        for i in range(len(nums)-2):
            l=nums[i:i+3]
            if 2*(l[0]+l[2])==l[1]:
                c+=1
        return c