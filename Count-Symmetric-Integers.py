class Solution:
    def countSymmetricIntegers(self, l: int, h: int) -> int:
        c=0
        for i in range(l,h+1):
            s=str(i)
            if len(s)%2==0:
                m=len(s)//2
                if sum(map(int,s[:m]))==sum(map(int,s[m:])):
                    c+=1
        return c