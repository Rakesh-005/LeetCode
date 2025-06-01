class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        l = len(p)
        p_sorted = sorted(p)
        
        for i in range(len(s) - l + 1):  # window of size len(p)
            if sorted(s[i:i + l]) == p_sorted:
                res.append(i)
        
        return res