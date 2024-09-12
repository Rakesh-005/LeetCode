class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        c=0
        a=set(allowed)
        for i in words:
            for j in i:
                if j not in a:
                    c+=1
                    break
        return len(words)-c