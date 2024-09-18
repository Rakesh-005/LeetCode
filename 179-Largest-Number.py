class Solution(object):
    def largestNumber(self, nums):
        \\\
        :type nums: List[int]
        :rtype: str
        \\\
        l=list(map(str,nums))
        l.sort(key=lambda x:x*10,reverse=True)
        if l[0]=='0':
            return '0'
        return ''.join(l)