class Solution:
    def minMovesToMakePalindrome(self, s):
        ans, count = list(s), 0 

        while ans:
            idx = ans.index(ans[-1])

            if idx == len(ans)-1:
                count += idx//2 
            else:
                count += idx 
                ans.pop(idx)
            ans.pop()

        return count