class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n=len(colors)
        l=0
        c=0
        for r in range(1,n+k-1):
            if colors[r%n]==colors[(r-1)%n]:
                l=r
            if r-l+1>=k:
                c+=1
            print(l,r,c)
        return c