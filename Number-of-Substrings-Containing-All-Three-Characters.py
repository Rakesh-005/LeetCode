class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        res = 0
        left = 0
        char_count = {'a': 0, 'b': 0, 'c': 0}
        
        for right in range(len(s)):
            char_count[s[right]] += 1
            
            while 0 < char_count['a'] and 0 < char_count['b'] and 0 < char_count['c']:
                res += len(s) - right
                char_count[s[left]] -= 1
                left += 1
        
        return res