# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildBST(self,l,r,nums):
        if l > r:
            return None
        
        m = (l + r)//2
        root = TreeNode(nums[m])
        
        root.left = self.buildBST(l,m-1,nums)
        root.right = self.buildBST(m+1,r,nums)
        return root
        
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        arr = []
        
        while head != None:
            arr.append(head.val)
            
            head = head.next
            
        return self.buildBST(0,len(arr)-1,arr)
