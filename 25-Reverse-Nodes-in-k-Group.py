# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        # Step 1: Extract all elements from the linked list into a list
        if not head:
            return None
        elements = []
        current = head
        while current:
            elements.append(current.val)
            current = current.next
        
        for i in range(0, len(elements), k):
            if i + k <= len(elements):
                elements[i:i+k] = elements[i:i+k][::-1]
        
        current = head
        for value in elements:
            current.val = value
            current = current.next
        
        return head
