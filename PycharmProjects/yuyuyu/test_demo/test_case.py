# -*- coding: utf-8 -*- 
# @Time : 2021/5/2 下午5:43 
# @Author : yuxiaoxue
# @File : test_case.py

import pytest
'''
pytest默认不输出打印信息，要通过添加-s的指令添加
-v
-rA  简单显示
pytest中的setup和teardown，一般可以通过配置文件进行管理--conftest.py

'''
# 前置与后置,只在类外有效
def setup_function():
    print('sfunction')

def teardown_function():
    print('tfunction')

def setup_module():
    print('smodule')

def teardown_module():
    print('tmodule')

@pytest.mark.testui
def xixi(xiyue):
    print('test02---')

def test_01(xiyue02):
    assert xiyue02 == 1, '失败'

#pytest中类的定义
class TestDemo:
    def setup(self):
        print('inside setup')

    def teardown(self):
        print('inside teardown')

    def test_d1(self):
        print('testd1')

    def test_d2(self):
        print('testd2')



#问题：这个没运行起来
if __name__ == '__main__':
    pytest.main(['-s','test_case.py'])
