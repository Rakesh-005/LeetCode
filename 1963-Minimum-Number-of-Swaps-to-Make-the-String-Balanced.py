class Solution:
    def minSwaps(self, s: str) -> int:
        a=0
        for i in s:
            if i=='[':
                a+=1
            elif a>0:
                a-=1
        return (a+1)//2