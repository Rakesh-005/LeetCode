class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True

        tmp = 1
        while tmp < n:
            tmp *= 3
            if n == tmp:
                return True

        return False