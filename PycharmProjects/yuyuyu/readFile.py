# -*- coding: utf-8 -*- 
# @Time : 2021/4/23 下午12:18 
# @Author : yuxiaoxue
# @File : readFile.py
#
# with open('pi_digits.txt') as file_pi:
#     contents = file_pi.read()
#     print(contents)
#
# with open('pi_digits.txt') as file_pi:
#     for line in file_pi:
#         print(line.rstrip())

with open('pi_digits.txt') as file_pi:
    lines = file_pi.readlines()
str = ''
for line in lines:
    str += line.strip()
birthDay = input('请输入你的生日：')
if birthDay in str:
    print('你的生日在圆周率中')
else:
    print('你的生日不在圆周率中')
    print(birthDay)
print(str[:22] + '...')
print(len(str))