class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        l=[]
        l.append(list(set(nums1).difference(set(nums2))))
        l.append(list(set(nums2).difference(set(nums1))))
        return l