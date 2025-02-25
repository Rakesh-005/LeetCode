class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        l=[]
        for i in words:
            for j in words:
                if i!=j and i in j and i not in l:
                    l.append(i)
        return l