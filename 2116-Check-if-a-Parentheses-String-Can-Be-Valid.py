class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s)%2==1:
            return False
        op=cp=0
        for i in range(len(s)):
            op+=1 if s[i]=='(' or locked[i]=='0' else -1
            if op<0:
                return False
        for i in range(len(s)-1,-1,-1):
            cp+=1 if locked[i]=='0' or s[i]==')' else -1
            if cp<0:
                return False
        return True