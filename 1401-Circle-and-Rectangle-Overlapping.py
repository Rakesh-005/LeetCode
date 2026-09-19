class Solution(object):
    def checkOverlap(self, r, cx, cy, x1, y1, x2, y2):
        """
        :type radius: int
        :type xCenter: int
        :type yCenter: int
        :type x1: int
        :type y1: int
        :type x2: int
        :type y2: int
        :rtype: bool
        """
        x = max(x1, min(cx, x2)) - cx
        y = max(y1, min(cy, y2)) - cy

        return x * x + y * y <= r * r