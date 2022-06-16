class Solution:
    
    #Function to return the diameter of a Binary Tree.
    def max_depth(self, root):
        if root == None:
            return 0
            
        lh = self.max_depth(root.left)
        rh = self.max_depth(root.right)
        
        return 1+max(lh,rh)
        
        
    def diameter(self,root):
        # Code here
        if root == None:
            return 0
            
        
        #heigt of left subtree
        lh = self.max_depth(root.left)
        #hight of right subtree
        rh = self.max_depth(root.right)
        
        
        
        return max(1+lh+rh,self.diameter(root.left),self.diameter(root.right))
