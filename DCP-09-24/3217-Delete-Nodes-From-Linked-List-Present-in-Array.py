# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def modifiedList(self, nums, head):
        """
        :type nums: List[int]
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        ns=set(nums)
        ptr=head
        Dummy=ListNode(0)
        curr=Dummy
        while ptr:
            if ptr.val not in ns:
                curr.next=ListNode(ptr.val)
                curr=curr.next
            ptr=ptr.next
        return Dummy.next