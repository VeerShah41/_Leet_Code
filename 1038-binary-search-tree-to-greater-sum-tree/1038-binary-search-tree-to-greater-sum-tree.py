# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def bstToGst(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        
        self.s = 0

        def dfs(node):
            if not node:
                return

            dfs(node.right)
            self.s += node.val
            node.val = self.s
            dfs(node.left)

        dfs(root)
        return root

        

        