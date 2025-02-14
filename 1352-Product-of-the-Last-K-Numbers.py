class ProductOfNumbers(object):

    def __init__(self):
        self.l=[1]

    def add(self, num):
        """
        :type num: int
        :rtype: None
        """
        if num==0:
            self.l=[1]
        else:
            self.l.append(self.l[-1]*num)

    def getProduct(self, k):
        """
        :type k: int
        :rtype: int
        """
        if len(self.l)<=k:
            return 0
        else:
            return self.l[-1]//self.l[-k-1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)