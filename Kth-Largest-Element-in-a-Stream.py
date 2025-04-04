class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k=k
        self.minheap=nums
        heapq.heapify(self.minheap)
        
    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        heapq.heappush(self.minheap,val)
        while len(self.minheap)>self.k:
            heapq.heappop(self.minheap)
        return self.minheap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)