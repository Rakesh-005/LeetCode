class Solution:
    def nextGreaterElement(self, n: int) -> int:
        l = list(str(n))                # convert number to list of digits (as characters)
        i = len(l) - 2
        while i >= 0 and l[i] >= l[i+1]:  # find first decreasing digit from right
            i -= 1
        if i < 0:                         # if whole number is decreasing
            return -1

        j = len(l) - 1
        while l[i] >= l[j]:              # find next bigger digit on right
            j -= 1
        l[i], l[j] = l[j], l[i]          # swap them

        l[i+1:] = l[i+1:][::-1]          # reverse the rest (make it smallest)

        a = int(''.join(l))              # convert back to int
        return a if a < 2**31 else -1    # check 32-bit constraint
