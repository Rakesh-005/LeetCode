class Solution(object):
    def takeCharacters(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n=len(s)
        a,b,c=0,0,0
        l,r=0,0
        ans=n
        ta,tb,tc=s.count('a'),s.count('b'),s.count('c')
        if ta<k or tb<k or tc<k:
            return -1
        while r<n:
            if s[r]=='a': a+=1
            elif s[r]=='b': b+=1
            else: c+=1
            r+=1
            while a+k>ta or b+k>tb or c+k>tc:
                if s[l]=='a': a-=1
                elif s[l]=='b': b-=1
                else: c-=1
                l+=1
            ans=min(ans,n-r+l)
        return ans