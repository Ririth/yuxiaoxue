# -*- coding: utf-8 -*- 
# @Time : 2021/3/21 下午9:41 
# @Author : yuxiaoxue
# @File : toOffer6.py

# @param pHead ListNode类
# @param k int整型
# @return ListNode类
#
class Solution:



    def FindKthToTail(self , pHead , k ):
        newlist = []
        if pHead == None:
            return None
        while pHead != None:
            newlist.append(pHead)
            print(newlist)
            pHead = pHead.next
        if k < 1 or k > len(newlist):
            return None
        else:
            print(newlist[-k])
            return newlist[-k]
    def FindKthToTail2(self,pHead,k):
        if k < 1 or pHead == None:
            return None
        fastNode = pHead
        for i in range(k-1):
            if fastNode.next != None:
                fastNode = fastNode.next
            else:
                return fastNode.next
        while fastNode.next != None:
            fastNode = fastNode.next
            pHead = pHead.next
        return pHead
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


if __name__ == '__main__':
    Node1 = ListNode(1)
    Node2 = ListNode(2)
    Node3 = ListNode(3)
    Node4 = ListNode(4)
    Node5 = ListNode(5)
    Node1.next = Node2
    Node2.next = Node3
    Node3.next = Node4
    Node4.next = Node5
    Node5.next = None
    self = " "

    if not Solution.FindKthToTail2(self, Node1, 6):
        print(Solution.FindKthToTail2(self, Node1, 6))
    else:
        print(Solution.FindKthToTail2(self, Node1, 6).val)
