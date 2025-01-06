class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        l = [0] * len(boxes)
        for i in range(len(boxes)):
            c = 0
            for j in range(len(boxes)):  
                if boxes[j] == '1': 
                    c += abs(j - i) 
            l[i] = c 
        return l
