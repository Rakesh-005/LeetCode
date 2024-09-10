# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        ptr = head
        while ptr and ptr.next:
            gcd_val = math.gcd(ptr.val, ptr.next.val)
            gcd_node = ListNode(gcd_val)
            gcd_node.next = ptr.next
            ptr.next = gcd_node
            ptr = gcd_node.next
        
        return head