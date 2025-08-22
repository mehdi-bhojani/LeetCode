#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
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
    maxDiameter=0
    def heightOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        left = self.heightOfBinaryTree(root.left)
        right = self.heightOfBinaryTree(root.right)
        self.maxDiameter = max(self.maxDiameter, left + right)
        return max(left,right)+1

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.heightOfBinaryTree(root)

        return self.maxDiameter
        
# @lc code=end

