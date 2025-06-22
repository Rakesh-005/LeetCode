class Solution(object):
    def divideString(self, s, k, fill):
        """
        :type s: str
        :type k: int
        :type fill: str
        :rtype: List[str]
        """

        if not s:
            return []
            
        result = []
        n = len(s)
        i = 0
        while i < n:
            result.append(s[i:i+k])
            i += k

        if len(result[-1]) < k:
            result[-1] += fill * (k - len(result[-1])) 

        return result