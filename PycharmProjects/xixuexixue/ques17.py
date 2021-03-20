# -*- coding: utf-8 -*- 
# @Time : 2021/3/20 下午5:20 
# @Author : yuxiaoxue
# @File : ques17.py

# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        if len(rotateArray) == 0:
            return 0
        n = 1
        for num in rotateArray:
            if num > rotateArray[n]:
                return rotateArray[n]
            else:
                n = n + 1
    array1 = [1,2]
    self = ''
    print(minNumberInRotateArray(self,array1))