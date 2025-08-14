class Solution:
    def largestGoodInteger(self, num: str) -> str:
        max_num: str = ""
        n: int = len(num)
        for i in range(n - 2):
            if num[i] == num[i + 1] == num[i + 2]:
                if max_num == '' or num[i] > max_num[0]:
                    max_num = num[i:i + 3]
        return max_num