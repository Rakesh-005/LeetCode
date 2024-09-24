class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        d={}
        for i in arr1:
            s=str(i)
            pr=''
            for i in s:
                pr+=i
                d[pr]=d.get(pr,0)+1
        ml=0
        for i in arr2:
            s=str(i)
            pr=''
            for i in s:
                pr+=i
                if pr in d:
                    ml=max(ml,len(pr))
        return ml