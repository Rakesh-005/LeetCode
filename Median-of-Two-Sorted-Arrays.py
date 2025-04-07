class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l=sorted(nums1+nums2)
        n=len(l)
        mid=n//2
        if n%2==0:
            return (l[mid-1]+l[mid])/2.0
        return l[mid]