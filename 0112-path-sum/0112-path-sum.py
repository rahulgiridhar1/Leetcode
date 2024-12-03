# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        val = 0
        def check(val, root):
            if not root:
                return False
            val += root.val

            if val==targetSum and not root.left and not root.right:
                return True 
            return check(val,root.left)or check(val,root.right)
        return check(0, root)


        