from typing import List
from collections import Counter

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        l = [num for row in grid for num in row]  # Flatten grid
        count = Counter(l)  # Get counts of each number
        n = len(l)
        
        repeated = next(num for num, freq in count.items() if freq == 2)
        missing = next(i for i in range(1, n + 1) if i not in count)

        return [repeated, missing]
