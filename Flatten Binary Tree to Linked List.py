# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightMost(self,root):
        
        while root.right != None:
            root=root.right
        
        return root
    
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root == None:
            return
        if root.right == None and root.left == None:
            return
        if root.left != None: 
            self.flatten(root.left)
        
        if root.right != None:
            self.flatten(root.right)
        
        
           
        t = root.right
        if root.left != None:
            root.right = root.left
            newnode=self.rightMost(root.left)
            newnode.right = t
            root.left = None
        
        return
