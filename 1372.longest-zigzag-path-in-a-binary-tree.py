# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max = 0

    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.max = 0
        self.helper(root, "")
        return self.max

    def helper(self, root, come_from):
      """
      For every node we will pass information like from which side it comes Left or Right.
      If it comes from the left then we will return the zigzag value of the right side and vice versa.
      And before return we will put max value of zigzag till now.
      """
        if not root:
            return 0

        l = self.helper(root.left, "L")
        r = self.helper(root.right, "R")

        if come_from == "L":
            self.max = max(self.max, r+1)
            return r+1
        elif come_from == "R":
            self.max = max(self.max, l+1)
            return l+1
        else:
            return 0
