# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root):
            if not root:
                return [0,root]
            [ld,ln]=dfs(root.left)
            [rd,rn]=dfs(root.right)
            if ld==rd:
                return [ld+1,root]
            elif ld>rd:
                return [ld+1,ln]
            else:
                return [rd+1,rn]
        return dfs(root)[1]