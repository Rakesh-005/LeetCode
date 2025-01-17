class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        x=0
        for i in derived:
            x^=i
        return x==0