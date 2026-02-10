# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        l=[]
        def ino(l,root):
            if not root:
                return []
            ino(l,root.left)
            l.append(root.val)
            ino(l,root.right)
        
        ino(l,root)
        return l