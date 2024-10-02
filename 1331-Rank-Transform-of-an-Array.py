class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        d={}
        arr1=sorted(list(set(arr)))
        for i in range(len(arr1)):
            d[arr1[i]]=i+1
        for i in range(len(arr)):
            arr[i]=d[arr[i]]
        return arr