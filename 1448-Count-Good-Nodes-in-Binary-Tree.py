class Solution:
    def maximum69Number (self, num: int) -> int:
        t=num
        s=str(num)
        for i in range(len(s)):
            if s[i]=='6':
                v=int(s[:i]+'9'+s[i+1:])
            else:
                v=int(s[:i]+\6\+s[i+1:])
            t=max(t,v)
        return t