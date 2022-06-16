class Solution:
    #Function to convert a binary tree into its mirror tree.
    def mirror(self,root):
        # Code here
        if root == None:
            return
        
        self.mirror(root.left)
        self.mirror(root.right)
        
        t = root.left
        root.left = root.right
        root.right = t
        
        return
