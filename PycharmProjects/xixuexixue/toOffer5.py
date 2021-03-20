# -*- coding: utf-8 -*- 
# @Time : 2021/3/20 下午9:34 
# @Author : yuxiaoxue
# @File : toOffer5.py

'''
题目描述：
输入一个链表，从尾到头打印链表的值
返回值：列表
'''

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        newList = []
        if listNode != None:
            if listNode.next != None:
                newList = self.printListFromTailToHead(listNode.next)
            newList.append(listNode.val)
        return newList

