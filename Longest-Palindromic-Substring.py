class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        max_len = 0
        res = \\
        
        for i in range(n):
            for j in range(n-1, i-1, -1):
                if s[i] == s[j]:
                    substr = s[i:j+1]
                    if substr == substr[::-1]:  # Check palindrome
                        if len(substr) > max_len:
                            max_len = len(substr)
                            res = substr
                        break  # No need to check shorter substrings ending at j
        return res
