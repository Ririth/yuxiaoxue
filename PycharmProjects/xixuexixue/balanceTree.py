# -*- coding: utf-8 -*- 
# @Time : 2021/4/24 下午2:36 
# @Author : yuxiaoxue
# @File : balanceTree.py

'''
输入一棵二叉树的根节点，判断该树是不是平衡二叉树。
如果某二叉树中任意节点的左右子树的深度相差不超过1，
那么它就是一棵平衡二叉树。

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        if root == None:
            return True
