#!/usr/bin/env python
# -*- coding:utf-8 -*-


class Item(object):
    """框架设计的Item类,提供了data属性保存解析后的数据"""
    def __init__(self,data):
        # data表示传入的数据
        self._data = data  # 设置为简单的私有属性

    @property
    def data(self):
        '''对外提供data进行访问，一定程度达到保护的作用'''
        return self._data
