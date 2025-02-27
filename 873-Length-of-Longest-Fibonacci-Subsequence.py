from typing import List

class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        s = set(arr)  # Convert array to a set for quick lookups
        max_length = 0
        
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                l = [arr[i], arr[j]]  # Start the sequence with two numbers
                
                while l[-1] + l[-2] in s:  # Check if the sum of last two elements exists in arr
                    l.append(l[-1] + l[-2])
                
                max_length = max(max_length, len(l))  # Update max length
        
        return max_length if max_length > 2 else 0  # Return 0 if no valid sequence found
