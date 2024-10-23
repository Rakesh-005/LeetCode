# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(arr):
            if not arr:
                return 
            ts=0
            for i in arr:
                if i.left:
                    ts+=i.left.val
                if i.right:
                    ts+=i.right.val
            ca=[]
            for i in arr:
                cs=0
                if i.left:
                    cs+=i.left.val
                if i.right:
                    cs+=i.right.val
                if i.left:
                    i.left.val=ts-cs
                    ca.append(i.left)
                if i.right:
                    i.right.val=ts-cs
                    ca.append(i.right)
            dfs(ca)

        arr=[root]
        root.val=0
        dfs(arr)
        return root