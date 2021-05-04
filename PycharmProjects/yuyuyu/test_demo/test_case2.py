# -*- coding: utf-8 -*- 
# @Time : 2021/5/3 下午3:04 
# @Author : yuxiaoxue
# @File : test_case2.py

import pytest

@pytest.mark.testui
def test_case01():
    print('markui')

#标签，可以添加多个标签
@pytest.mark.interface
def test_case02():
    print('markinterface')

if __name__ == '__main__':
    pytest.main('-s')