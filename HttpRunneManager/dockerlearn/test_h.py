# -*-coding:utf-8-*-
# @作者：haiyu.ma
# @创建日期：2021-03-22 23:51 
# @Software：PyCharm
# ----------------------------------------------------------------------------
import pytest

def test_one():
    print("正在执行---test one")
    x = "this"
    assert 'h' in x

def test_two():
    print("正在执行---test two")
    x = "hello"
    assert x

def test_three():
    print("正在执行---test three")
    a = "hello"
    b = "hello world"
    assert a in b

if __name__ == '__main__':
    pytest.main(["-s","test_h.py"])