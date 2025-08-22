#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#
from typing import Optional
# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hieghtOfBTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        height = max(self.hieghtOfBTree(root.left), self.hieghtOfBTree((root.right)))

        return height+1
    

    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        holeft= self.hieghtOfBTree(root.left)
        horight = self.hieghtOfBTree(root.right)

        return abs(holeft - horight) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
        
# @lc code=end

