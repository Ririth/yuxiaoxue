# -*- coding: utf-8 -*- 
# @Time : 2021/5/2 下午9:11 
# @Author : yuxiaoxue
# @File : conftest.py

'''
@pytest.fixture()
定义一个基本的setup和teardown----预置函数
预置函数用于前期的数据准备
setup和teardown的配置文件
fixture---一大利器
scope定义了四种不同的等级---默认等级是function
session：在本次session级别中只执行一次
module：模块级别中只执行一次
class：在类级别中只执行一次
function：在函数级别只执行一次，每一个函数只执行一次
'''
import pytest

@pytest.fixture()
def xiyue():
    print('喜悦pytest')

@pytest.fixture()
def xiyue02():
    return 1