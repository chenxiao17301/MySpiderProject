#!/usr/bin/env python
# -*- coding:utf-8 -*-

from ..http.request import Request
from ..items import Item


class Spider(object):

    # start_url = "http://www.baidu.com/"

    start_urls = []
    def start_requests(self):
        """
        返回第一个入口请求给引擎
        :return:
        """
        for start_url in self.start_urls:
            yield Request(start_url)

    def parse(self, response):
        """解析response返回item给引擎(-->管道)
        """
        # content = {"content" : response.body}
        # content = response.body
        # item = Item(content)
        # return item
        raise Exception(u"必须重写父类Spider的parse方法")

"""
爬虫组件功能：

构建请求信息(初始的)，也就是生成请求对象(Request)
解析响应对象，返回数据对象(Item)或者新的请求对象(Request)
实现方案：

实现start_requests方法，返回请求对象
实现parse方法，返回Item对象或者新的请求对象
"""