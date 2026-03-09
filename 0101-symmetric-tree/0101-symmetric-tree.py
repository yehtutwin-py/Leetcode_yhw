# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def check(left_node,right_node):
            if not left_node and not right_node:
                return True
            if not left_node or not right_node or left_node.val!=right_node.val:
                return False
            return check(left_node.left,right_node.right) and check(right_node.left,left_node.right)
        return check(root.left,root.right)
        