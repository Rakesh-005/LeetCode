# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def b(root,l):
            if not root:
                return 
            b(root.left,l)
            l.append(root.val)
            b(root.right,l)
        nums=[]
        b(root,nums)
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==k:
                    return True
        return False
        