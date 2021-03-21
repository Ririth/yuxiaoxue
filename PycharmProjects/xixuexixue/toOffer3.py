# -*- coding: utf-8 -*- 
# @Time : 2021/3/20 下午11:49 
# @Author : yuxiaoxue
# @File : toOffer3.py

'''
牛客最近来了一个新员工Fish，每天早晨总是会拿着一本英文杂志，
写些句子在本子上。同事Cat对Fish写的内容颇感兴趣，
有一天他向Fish借来翻看，但却读不懂它的意思。
例如，“student. a am I”。后来才意识到，
这家伙原来把句子单词的顺序翻转了，
正确的句子应该是“I am a student.”。
Cat对一一的翻转这些单词顺序可不在行，你能帮助他么？
'''

class Solution:
    def ReverseSentence(self, s):
        newList = []
        newList = s.split(' ')
        l = len(newList)
        for i in range(l-1,-1,-1):
             newList.append(newList[i])
        newList = newList[l:2*l]
        s =  " ".join(newList)
        return s


    def ReverseSentence2(self,s):
        s = s.split(' ')
        s = s[::-1]
        return ' '.join(s)

    self = ''
    s = 'nowcoder. a am I'
    print(ReverseSentence2(self,s))
    # l = s.split(' ')
    # print(l)
    # print(l[0:2])
