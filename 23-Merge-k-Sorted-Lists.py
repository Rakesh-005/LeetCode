# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        \\\
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        \\\
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