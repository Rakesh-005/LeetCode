# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head or not head.next or k == 0:
            return head
        
        # Step 1: Extract all elements into a list
        elements = []
        current = head
        while current:
            elements.append(current.val)
            current = current.next
        
        # Step 2: Rotate the list
        n = len(elements)
        k %= n  # Handle cases where k > n
        if k > 0:
            elements = elements[-k:] + elements[:-k]
        
        # Step 3: Dump the rotated data back into the linked list
        current = head
        for value in elements:
            current.val = value
            current = current.next
        
        return head
