# -*- coding: utf-8 -*- 
# @Time : 2021/4/24 下午3:40 
# @Author : yuxiaoxue
# @File : levelTraversal.py
from queue import Queue
'''
题目描述：

从上往下打印出二叉树的每个节点，同层节点从左至右打印。
输入：{5,4,#,3,#,2,#,1}
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        if root == None:
            return None
        q = Queue()
        q.put(root)
        queuelist = []
        queuelist.append(root)
        while queuelist:
            root = q.get()
            if root.left:
                q.put(root.left)
                queuelist.append(root.left)
            if root.right:
                q.put(root.right)
                queuelist.append(root.right)
        return queuelist

if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = None
    root.left.left = TreeNode(3)
    root.left.right = None
    s = Solution()
    print(s.PrintFromTopToBottom(root))





