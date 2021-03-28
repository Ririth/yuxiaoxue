# -*- coding: utf-8 -*- 
# @Time : 2021/3/27 下午5:23 
# @Author : yuxiaoxue
# @File : toOffer7.py

class CQueue(object):
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def appendTail(self, value):
        self.stack1.append(value)
        print(self.stack1)
    def deleteHead(self):
        if(len(self.stack1)==0 and len(self.stack2)==0):
            return -1
        elif(self.stack2):
                return self.stack2.pop()
        else:
            while(self.stack1):
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()


if __name__ == '__main__':
    c = CQueue()
    c.appendTail(3)
    c.appendTail(2)
    print(c.deleteHead())
    print(c.deleteHead())










'''
用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，
分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead 操作返回 -1 )
'''
