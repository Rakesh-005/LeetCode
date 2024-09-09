# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        res = []
        ptr = head
        while ptr:
            res.append(ptr.val)
            ptr = ptr.next
        l = [[-1] * n for _ in range(m)]
        top, bottom, left, right = 0, m-1, 0, n-1
        index = 0
        
        while top <= bottom and left <= right:
            for j in range(left, right + 1):
                if index < len(res):
                    l[top][j] = res[index]
                    index += 1
            top += 1

            for i in range(top, bottom + 1):
                if index < len(res):
                    l[i][right] = res[index]
                    index += 1
            right -= 1
            
            for j in range(right, left - 1, -1):
                if index < len(res):
                    l[bottom][j] = res[index]
                    index += 1
            bottom -= 1
            
            for i in range(bottom, top - 1, -1):
                if index < len(res):
                    l[i][left] = res[index]
                    index += 1
            left += 1
        
        return l