# -*- coding: utf-8 -*- 
# @Time : 2021/5/2 下午1:40 
# @Author : yuxiaoxue
# @File : isSubStructure.py

'''
输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)

B是A的子结构， 即 A中有出现和B相同的结构和节点值。

例如:
给定的树 A:

     3
    / \
   4   5
  / \
 1   2
给定的树 B：

   4 
  /
 1
返回 true，因为 B 与 A 的一个子树拥有相同的结构和节点值。
'''

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSubStructure(self, A, B):
        """
        :type A: TreeNode
        :type B: TreeNode
        :rtype: bool
        """
        if not A or not B:
            return False
        if self.isSame(A,B):
            return True
        else:
            return (self.isSubStructure(A.left,B) or self.isSubStructure(A.right,B))

    def isSame(self,rootA,rootB):
        if not rootB:
            print('111')
            return True
        if not rootA:
            print('222')
            return False
        if rootA.val != rootB.val:
            print('333')
            return False
        print('444')
        return self.isSame(rootA.left,rootB.left) and self.isSame(rootA.right,rootB.right)


if __name__ == "__main__":
    rootA = TreeNode(8)
    rootA.left = TreeNode(8)
    rootA.right = TreeNode(7)
    rootA.left.left = TreeNode(9)
    rootA.left.right = TreeNode(3)
    rootA.left.right.left = TreeNode(4)
    rootA.left.right.right = TreeNode(7)
    rootB = TreeNode(8)
    rootB.left = TreeNode(9)
    rootB.right = TreeNode(2)
    s = Solution()
    print(s.isSubStructure(rootA,rootB))

















