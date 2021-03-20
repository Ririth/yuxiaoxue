# -*- coding: utf-8 -*- 
# @Time : 2021/3/20 下午10:43 
# @Author : yuxiaoxue
# @File : toOffer2.py

# @param s string字符串
# @return string字符串
#
import string

class Solution:
    def replaceSpace(self , s ):
        i = 0
        newList = list(s)
        for str in newList:
            if str == " ":
                newList[i] = '%20'
            i += 1
        return ''.join(newList)




    def replaceSpace2(self,s):
        ss = s.replace(' ','%20')
        return ss


    def replaceSpace3(self,s):
        s = s.split(' ')
        return '%20'.join(s)

    self = ''
    s = "We Are Happy"
    print(replaceSpace3(self,s))
