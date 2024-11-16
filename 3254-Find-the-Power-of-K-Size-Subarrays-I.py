class Solution(object):
    def resultsArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        results = []
        
        for i in range(n - k + 1):
            subarray = nums[i:i + k]
            if subarray == sorted(subarray) and len(set(subarray)) == len(subarray):
                if all(subarray[j] + 1 == subarray[j + 1] for j in range(len(subarray) - 1)):
                    results.append(max(subarray))
                else:
                    results.append(-1)
            else:
                results.append(-1)
        
        return results