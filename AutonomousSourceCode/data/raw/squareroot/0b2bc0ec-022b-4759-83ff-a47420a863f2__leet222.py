# encoding: utf8
'''
Count Complete Tree Nodes
Given a complete binary tree, count the number of nodes.

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

直接遍历超时。
根据完全二叉树的特点。
判断是否是完全二叉树，是的话直接计算出节点个数；否则递归的计算左子树和右子树。
'''

import unittest
from pprint import pprint
import pdb

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1: # TLE
    # @param {TreeNode} root
    # @return {integer}
    def countNodes(self, root):
        if root==None:
            return 0
        return 1+self.countNodes(root.left)+self.countNodes(root.right)

class Solution: 
    # @param {TreeNode} root
    # @return {integer}
    def countNodes(self, root):
        if root==None:
            return 0
        leftdepth=0
        rightdepth=0
        p=root
        while p.left:
            p=p.left
            leftdepth+=1
        p=root
        while p.right:
            p=p.right
            rightdepth+=1
        if leftdepth==rightdepth:
            return 2**(leftdepth+1)-1
        else:
            return 1+self.countNodes(root.left)+self.countNodes(root.right)

class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        a=['10100',
            '10111',
            '11111',
            '10010',]
        self.assertEqual(self.a.maximalSquare(a), 4)
        self.assertEqual(self.a.maximalSquare(["1"]), 1)
        a=["0001",
            "1101",
            "1111",
            "0111",
            "0111"]
        self.assertEqual(self.a.maximalSquare(a), 9)

if __name__ == '__main__':
    unittest.main()