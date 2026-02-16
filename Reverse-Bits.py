1class Solution:
2    def reverseBits(self, n: int) -> int:
3        return int(bin(n)[2:].zfill(32)[::-1],2)