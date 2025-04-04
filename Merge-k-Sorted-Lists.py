# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        l=[]
        for node in lists:
            while node:
                heapq.heappush(l,node.val)
                node=node.next
        d=ListNode(0)
        curr=d
        while l:
            curr.next=ListNode(heapq.heappop(l))
            curr=curr.next
        return d.next