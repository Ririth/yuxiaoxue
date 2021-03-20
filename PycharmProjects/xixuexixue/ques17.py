# -*- coding: utf-8 -*- 
# @Time : 2021/3/20 下午5:20 
# @Author : yuxiaoxue
# @File : ques17.py

# -*- coding:utf-8 -*-

'''
题目描述：
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
'''
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        l = len(rotateArray)
        if l == 0:
            return 0
        low = 0
        high = l - 1
        mid = int((low + high) / 2)
        while low != high:
            if rotateArray[0] <= rotateArray[mid]:
                low = mid + 1
                mid = int((low + high) / 2)
            else:
                high = mid
                low = 0
                mid = int((low + high) / 2)
        return rotateArray[mid]
    array1 = [1,2]
    self = ''
    print(minNumberInRotateArray(self,array1))