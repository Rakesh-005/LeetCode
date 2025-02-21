# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def b(root,l):
            if not root:
                return 
            b(root.left,l)
            l.append(root.val)
            b(root.right,l)
        l=[]
        b(root,l)
        return l[k-1] if k<=len(l) else -1