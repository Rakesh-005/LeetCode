class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        ch=Counter(s)
        sch=sorted(s, key=lambda x: (ch[x], x), reverse=True)
        return ''.join(sch)