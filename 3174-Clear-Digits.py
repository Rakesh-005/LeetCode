class Solution:
    def clearDigits(self, s: str) -> str:
        if len(s)==0:
            return ""
        l=[]
        for i in s:
            if i in '0123456789':
                l.pop(-1)
            else:
                l.append(i)
        return ''.join(l)