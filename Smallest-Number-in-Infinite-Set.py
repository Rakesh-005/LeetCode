class SmallestInfiniteSet:

    def __init__(self):
        self.d=set()
        self.i=[1]

    def popSmallest(self) -> int:
        s=heapq.heappop(self.i)
        self.d.add(s)
        if len(self.i)==0:
            heapq.heappush(self.i,s+1)
        return s

    def addBack(self, num: int) -> None:
        if num in self.d:
            heapq.heappush(self.i,num)
            self.d.remove(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)