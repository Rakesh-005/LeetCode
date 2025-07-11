# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr=head
        prev=None
        while ptr:
            a=ptr.next
            ptr.next=prev
            prev=ptr
            ptr=a
        return prev