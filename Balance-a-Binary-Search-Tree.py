1# Definition for a binary tree node.
2# class TreeNode(object):
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution(object):
8    def balanceBST(self, root):
9        """
10        :type root: TreeNode
11        :rtype: TreeNode
12        """
13        def dfs(node):
14            if node is None:
15                return 
16            dfs(node.left)
17            l.append(node.val)
18            dfs(node.right)
19        def create(le,r):
20            if le<=r:
21                m=(le+r)//2
22                return TreeNode(l[m],create(le,m-1),create(m+1,r))
23        l=[]
24        dfs(root)
25        return create(0,len(l)-1)