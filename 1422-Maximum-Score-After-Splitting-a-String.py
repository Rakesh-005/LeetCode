class Solution:
    def maxScore(self, s: str) -> int:
        # m=0
        # for i in range(len(s)-1):
        #     m=max(m,s[:i+1].count('0')+s[i+1:].count('1'))
        # return m
        m=0
        e=0
        o=s.count('1')
        for i in range(len(s)-1):
            if s[i]=='0':
                e+=1
            else:
                o-=1
            m=max(m,e+o)
        return m