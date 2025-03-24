class Solution(object):
    def countDays(self, days, m):
        """
        :type days: int
        :type meetings: List[List[int]]
        :rtype: int
        """
        m.sort()
        start, end = m[0]
        c=start-1 
        for x in range(1, len(m)):
            new_start, new_end = m[x]
            if new_start<=end:
                end = max(end, new_end)
            else:
                c+=new_start-end-1
                end = new_end
        return c+(days-end)
                