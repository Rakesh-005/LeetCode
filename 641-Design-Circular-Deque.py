class MyCircularDeque:

    def __init__(self, k: int):
        self.v=[-1]*k
        self.c=k
        self.f=0
        self.b=0
        self.s=0
    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.f==0:
            self.f=self.c-1
        else:
            self.f-=1
        self.v[self.f]=value
        self.s+=1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.v[self.b]=value
        if self.b==self.c-1:
            self.b=0
        else:
            self.b+=1
        self.s+=1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.v[self.f]=-1
        if self.f==self.c-1:
            self.f=0
        else:
            self.f+=1
        self.s-=1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        if self.b==0:
            self.b=self.c-1
        else:
            self.b-=1
        self.v[self.b]=-1
        self.s-=1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.v[self.f]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        if self.b==0:
            return self.v[self.c-1]
        else:
            return self.v[self.b-1]

    def isEmpty(self) -> bool:
        return self.s==0

    def isFull(self) -> bool:
        return self.s==self.c


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()