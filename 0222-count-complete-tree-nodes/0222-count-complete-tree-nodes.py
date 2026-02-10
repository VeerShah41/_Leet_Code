# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        l=[]
        def help(l,root):
            if not root:
                return[]
            l.append(root.val)
            help(l,root.left)
            help(l,root.right)
        help(l,root)
        return len(l)