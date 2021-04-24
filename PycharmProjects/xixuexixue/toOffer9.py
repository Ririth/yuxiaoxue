# -*- coding: utf-8 -*- 
# @Time : 2021/3/28 下午6:01 
# @Author : yuxiaoxue
# @File : toOffer9.py
class Solution(object):
    def fib(self, n):
        if(n==0):
            return 0
        if(n==1):
            return 1
        list1 = []
        list1.append(0)
        list1.append(1)

        if(n > 1):
            for i in list(range(2,n+1)):
                list1.append((list1[i-1] + list1[i-2])%1000000007)
        return list1[n]

if __name__ == '__main__':
    s = Solution()
    n = 45
    print(s.fib(n))

'''
题目描述：
斐波那契数列
写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项（即 F(N)）。斐波那契数列的定义如下：

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), 其中 N > 1.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/fei-bo-na-qi-shu-lie-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
