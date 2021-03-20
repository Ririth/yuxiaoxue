# -*- coding: utf-8 -*- 
# @Time : 2021/3/20 下午11:15 
# @Author : yuxiaoxue
# @File : toOffer4.py

'''
汇编语言中有一种移位指令叫做循环左移（ROL），
现在有个简单的任务，就是用字符串模拟这个指令的运算结果。
对于一个给定的字符序列S，请你把其循环左移K位后的序列输出。
例如，字符序列S=”abcXYZdef”,要求输出循环左移3位后的结果，
即“XYZdefabc”。是不是很简单？OK，搞定它
'''

class Solution:
    def LeftRotateString(self, s, n):
        newList = list(s)
        l = len(newList)
        if n > l:
            return ''.join(newList)
        for i in range(n):
            newList.append(s[i])
        ss = ''
        for i in range(n,len(newList)):
            ss += newList[i]
        return ss


    def LeftRotateString2(self,s,n):

        ss = s+s
        l = len(s)
        if n > l:
            return s

        return ss[n:n+l]

    s = "6yuxue"
    self = " "
    print(LeftRotateString2(self,s,3))
