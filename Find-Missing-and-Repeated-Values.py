class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        l=[]
        l1=[float('-inf')]*2
        for i in grid:
            for j in i:
                l.append(j)
        for i in set(l):
            if l.count(i)==2:
                l1[0]=i
        for i in range(1,len(l)+1):
            if i not in l:
                l1[1]=i
        return l1