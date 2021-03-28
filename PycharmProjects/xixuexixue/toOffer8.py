# -*- coding: utf-8 -*- 
# @Time : 2021/3/27 下午9:38 
# @Author : yuxiaoxue
# @File : toOffer8.py

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        if(preorder==None or inorder==None or len(preorder)==0 or len(inorder)==0):
            return None
        elif(len(preorder) != len(inorder)):
            return None
        root = TreeNode(preorder[0])
        for i in list(range(len(inorder))):
            if(root.val == inorder[i]):
                root.left = self.buildTree(preorder[1:i+1],inorder[:i])
                root.right = self.buildTree(preorder[i+1:],inorder[i+1:])
        return root

# 前序遍历 preorder = [3,9,20,15,7]
# 中序遍历 inorder = [9,3,15,20,7]

if __name__ == '__main__':
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    # print(preorder[1:2])
    # print(inorder[0:1])
    # list1 = range(0,1)
    # print(list1)
    self = ''
    s = Solution()
    print(s.buildTree(preorder,inorder))

'''
题目描述：
输入某二叉树的前序遍历和中序遍历的结果，
请重建该二叉树。
假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
'''