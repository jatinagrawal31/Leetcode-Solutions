
'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def checkSame(self, l, r):
        if(l == None and r == None):
            return True
        elif(l == None or r == None):
            return False
        elif(l.val == r.val):
            return self.checkSame(l.left, r.right) and self.checkSame(l.right, r.left)
        else:
            return False
        
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if(root == None):
            return True
        return self.checkSame(root.left, root.right)
        