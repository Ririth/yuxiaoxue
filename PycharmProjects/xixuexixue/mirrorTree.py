# -*- coding: utf-8 -*- 
# @Time : 2021/4/24 下午2:54 
# @Author : yuxiaoxue
# @File : mirrorTree.py
'''
题目描述：
操作给定的二叉树，将其变换为源二叉树的镜像。
比如：    源二叉树
            8
           /  \
          6   10
         / \  / \
        5  7 9 11
        镜像二叉树
            8
           /  \
          10   6
         / \  / \
        11 9 7  5
输入：
{8,6,10,5,7,9,11}
返回：
{8,10,6,11,9,7,5}
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# @param pRoot TreeNode类
# @return TreeNode类
#
class Solution:
    def Mirror(self , pRoot ):

        if pRoot == None:
            return None
        elif pRoot.left == None and pRoot.right == None:
            return pRoot
        pRoot.left,pRoot.right = pRoot.right,pRoot.left
        self.Mirror(pRoot.left)
        self.Mirror(pRoot.right)
        return pRoot
        # mirrorStack = []
        # while pRoot or mirrorStack:
        #     while pRoot:
        #         pRoot.left,pRoot.right = pRoot.right,pRoot.left
        #         mirrorStack.append(pRoot)
        #         pRoot = pRoot.left
        #     if mirrorStack:
        #         pRoot = mirrorStack.pop()
        #         pRoot = pRoot.right
        # return pRoot

if __name__=='__main__':
    pRoot = TreeNode(8)
    pRoot.left = TreeNode(6)
    pRoot.right = TreeNode(10)
    pRoot.left,pRoot.right = pRoot.right,pRoot.left

    s = Solution()
    root = s.Mirror(pRoot)
    print(root.val,root.left.val,root.right.val)