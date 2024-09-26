# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        ans=[]
        level=[root]
        while level:
            ans.append([node.val for node in level])
            l=[]
            for i in level:
                l.extend([i.left,i.right])
            level=[node for node in l if node]
        return ans[::-1]
