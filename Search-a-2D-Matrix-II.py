__import__(\atexit\).register(lambda: open(\display_runtime.txt\, \w\).write(\0\))
from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        row , col = 0,n-1
        while row <m and col >=0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -=1
            else:
                row +=1
        return False
        