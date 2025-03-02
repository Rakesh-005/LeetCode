class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        d = {}
        for i in nums1:
            if i[0] in d:
                d[i[0]] += i[1]
            else:
                d[i[0]] = i[1]
        for j in nums2:
            if j[0] in d:
                d[j[0]] += j[1]
            else:
                d[j[0]] = j[1]
        return [[k, v] for k, v in sorted(d.items())]
