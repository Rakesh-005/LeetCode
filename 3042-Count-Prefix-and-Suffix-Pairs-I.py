class Solution(object):
    def countPrefixSuffixPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        c=0
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if i<j and words[j].startswith(words[i]) and words[j].endswith(words[i]):
                    c+=1
        return c