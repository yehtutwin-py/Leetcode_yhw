# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        def binary(node):
            result=[]
            def helper(node):
                if not node:
                    result.append(None)
                    return
                else:
                    result.append(node.val)
                    helper(node.left)
                    helper(node.right)
            helper(node)
            return result
        print(binary(q))
        x=binary(p)
        y=binary(q)
        if x==y:
            return True
        else:   
            return False
            
        