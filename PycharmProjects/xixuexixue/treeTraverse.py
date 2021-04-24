# -*- coding: utf-8 -*- 
# @Time : 2021/4/11 下午5:55 
# @Author : yuxiaoxue
# @File : treeTraverse.py

'''
二叉树的非递归遍历
param：TreeNode

        3
       / \
      9  20
        /  \
       15   7
'''

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    #递归遍历
    list1 = []
    list2 = []
    list3 = []
    list4 = []
    list5 = []
    list6 = []
    list7 = []
    list8 = []
    def treePreorderTraverse(self,TreeNode):
        if TreeNode == None:
            return None
        self.list1.append(TreeNode)
        self.treePreorderTraverse(TreeNode.left)
        self.treePreorderTraverse(TreeNode.right)
        return self.list1

    def treeMidorderTraverse(self,TreeNode):
        if TreeNode == None:
            return None
        self.treeMidorderTraverse(TreeNode.left)
        self.list2.append(TreeNode)
        self.treeMidorderTraverse(TreeNode.right)
        return self.list2

    def treePostorderTraverse(self,TreeNode):
        if TreeNode == None:
            return None
        self.treePostorderTraverse(TreeNode.left)
        self.treePostorderTraverse(TreeNode.right)
        self.list3.append(TreeNode)

        return self.list3
    #非递归遍历
    def treePreorderTraverse1(self,TreeNode):
        preorderList = []
        if TreeNode == None:
            return None
        while(TreeNode or preorderList):
            if TreeNode != None:
                preorderList.append(TreeNode)
                self.list4.append(TreeNode)
                TreeNode = TreeNode.left
            elif TreeNode == None:
                TreeNode = preorderList.pop()
                TreeNode = TreeNode.right
        return self.list4

    def treePreorderTraverse2(self,TreeNode):
        preorderList = []
        if TreeNode == None:
            return None
        while(TreeNode or preorderList):
            while(TreeNode != None):
                preorderList.append(TreeNode)
                self.list5.append(TreeNode)
                TreeNode = TreeNode.left
            if preorderList != None:
                TreeNode = preorderList.pop()
                TreeNode = TreeNode.right
        return self.list5

    #非递归中序遍历
    def treeMidorderTraverse1(self,TreeNode):
        midorderList = []
        if TreeNode == None:
            return None
        while(TreeNode or midorderList):
            while(TreeNode != None):
                midorderList.append(TreeNode)
                TreeNode = TreeNode.left
            if midorderList !=None:
                TreeNode = midorderList.pop()
                self.list6.append(TreeNode)
                TreeNode = TreeNode.right
        return self.list6

    #非递归后序遍历
    def treePostorderTraverse1(self,TreeNode):
        postorderList = []
        flagNode = None
        if TreeNode == None:
            return None
        while (TreeNode or postorderList):
            while(TreeNode != None):
                postorderList.append(TreeNode)
                TreeNode = TreeNode.left
            if postorderList != None:
                TreeNode = postorderList[-1]
                if TreeNode.right and TreeNode.right != flagNode:
                    TreeNode = TreeNode.right
                else:
                    TreeNode = postorderList.pop()
                    self.list7.append(TreeNode)
                    flagNode = TreeNode
                    TreeNode = None
        return self.list7







if __name__ == '__main__':
    root = TreeNode(3)
    leftNode = TreeNode(9)
    rightNode = TreeNode(20)
    rightNodeleft = TreeNode(15)
    rightNoderight = TreeNode(7)
    root.left = leftNode
    root.right = rightNode
    rightNode.left = rightNodeleft
    rightNode.right = rightNoderight
    s = Solution()
    # list1 = s.treePreorderTraverse(root)
    # print('-----先序遍历----')
    # for node in list1:
    #     print(node.val)
    # list2 = s.treeMidorderTraverse(root)
    # print('-----中序遍历----')
    # for node in list2:
    #     print(node.val)
    # list3 = s.treePostorderTraverse(root)
    # print('-----后序遍历----')
    # for node in list3:
    #     print(node.val)
    # list4 = s.treePreorderTraverse1(root)
    # print('-----非递归先序遍历----')
    # for node in list4:
    #     print(node.val)

    # list5 = s.treePreorderTraverse2(root)
    # print('-----非递归先序遍历----')
    # for node in list5:
    #     print(node.val)

    # list = s.treeMidorderTraverse1(root)
    # print('-----非递归中序遍历----')
    # for node in list:
    #     print(node.val)
    # print(list[-1].val)

    list = s.treePostorderTraverse1(root)
    print('-----非递归中序遍历----')
    for node in list:
        print(node.val)




