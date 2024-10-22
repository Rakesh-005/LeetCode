# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        q=[root]
        root.level=0
        l=defaultdict(int)
        while q:
            node=q.pop()
            l[node.level]+=node.val
            if node.left:
                node.left.level=node.level+1
                q.append(node.left)
            if node.right:
                node.right.level=node.level+1
                q.append(node.right)
        l2=[l[i] for i in l]
        if k>len(l2):
            return -1
        return sorted(l2)[-k]