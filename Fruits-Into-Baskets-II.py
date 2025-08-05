class Solution(object):
    def numOfUnplacedFruits(self, fruits, baskets):
        """
        :type fruits: List[int]
        :type baskets: List[int]
        :rtype: int
        """
        count=0
        for i in fruits:
            for j in range(len(baskets)):
                if i<=baskets[j]:
                    count+=1
                    baskets[j]=-1
                    break
        return len(fruits)-count