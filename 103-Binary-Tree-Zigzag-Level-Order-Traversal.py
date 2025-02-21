# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        ans=[]
        level=[root]
        even=False
        while level:
            if even:
                ans.append([node.val for node in level][::-1])
            else:
                ans.append([node.val for node in level])
            l=[]
            for i in level:
                l.extend([i.left,i.right])
            level=[node for node in l if node]
            even=not even
        return ans