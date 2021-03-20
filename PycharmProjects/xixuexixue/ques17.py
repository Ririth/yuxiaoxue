# -*- coding: utf-8 -*- 
# @Time : 2021/3/20 下午5:20 
# @Author : yuxiaoxue
# @File : ques17.py

# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        l = len(rotateArray)
        if l == 0:
            return 0
        low = 0
        high = l - 1
        mid = int((low + high) / 2)
        while low != high:
            if rotateArray[0] == rotateArray[mid]:
                if rotateArray[0] > rotateArray[1]:
                    return rotateArray[1]
                else:
                    return rotateArray[0]
            elif rotateArray[0] < rotateArray[mid]:
                low = mid + 1
                mid = int((low + high) / 2)
            else:
                high = mid
                low = 0
                mid = int((low + high) / 2)
        return rotateArray[mid]
    array1 = [3,4,5,6,1,2]
    self = ''
    print(minNumberInRotateArray(self,array1))