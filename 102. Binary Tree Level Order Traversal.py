
# print values of a binary tree level by level.
#                       3
#                   5       7
#               2      3  1    9
#
#ans: [[3],[5,7],[2,3,1,9]]
#
#
#
#
#




# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        if root == None:
            return []
        queue=[root]
        res=[[root.val]]
        
        while(len(queue)>0):
            length=len(queue)
            
            temp=[]
            
            while length:
                node=queue.pop()
                if node.left != None:
                    queue.insert(0,node.left)
                    temp.append(node.left.val)

                if node.right != None:
                    queue.insert(0,node.right)
                    temp.append(node.right.val)
                    
                length -= 1
            
            if len(temp)>0:
                res.append(temp)
            
        return res
            
        
