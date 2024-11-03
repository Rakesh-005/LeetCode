# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        all_values = []
        for lst in lists:
            while lst:
                all_values.append(lst.val)
                lst = lst.next
        all_values.sort()
        dummy = ListNode() 
        current = dummy
        for value in all_values:
            current.next = ListNode(value)
            current = current.next
        return dummy.next