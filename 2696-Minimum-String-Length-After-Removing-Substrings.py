class Solution:
    def minLength(self, s: str) -> int:
        l=[]
        for i in s:
            if not l:
                l.append(i)
                continue
            if l[-1]=='A' and i=='B':
                l.pop()
            elif l[-1]=='C' and i=='D':
                l.pop()
            else:
                l.append(i)
        return len(l)