# -*- coding: utf-8 -*- 
# @Time : 2021/3/20 下午5:20 
# @Author : yuxiaoxue
# @File : ques17.py

# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        if len(rotateArray) == 0:
            return 0
        n = 0
        for num in rotateArray:
            if num < n:
                return num
            else:
                n = num

    array1 = [1,2]
    self = ''
    print(minNumberInRotateArray(self,array1))