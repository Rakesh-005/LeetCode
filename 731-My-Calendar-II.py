class MyCalendarTwo:

    def __init__(self):
        self.si=[]
        self.do=[]
    def book(self, start: int, end: int) -> bool:
        for s,e in self.do:
            if start<e and end>s:
                return False
        for s,e in self.si:
            if start<e and end>s:
                self.do.append((max(start,s),min(end,e)))
        self.si.append((start,end))
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)