class AllOne:

    def __init__(self):
        self.d={}

    def inc(self, key: str) -> None:
        if key in self.d:
            self.d[key]+=1
        else:
            self.d[key]=1

    def dec(self, key: str) -> None:
        if key in self.d:
            if self.d[key]>1:
                self.d[key]-=1
            else:
                self.d.pop(key)

    def getMaxKey(self) -> str:
        if not self.d:
            return \\
        m=max(self.d.values())
        for key in self.d.keys():
            if self.d[key]==m:
                return key

    def getMinKey(self) -> str:
        if not self.d:
            return \\
        m=min(self.d.values())
        for key in self.d.keys():
            if self.d[key]==m:
                return key


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()