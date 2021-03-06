#coding:utf-8


class Request(object):
    """
        框架提供的请求对象类，用来添加一些参数
    """
    def __init__(self, url, method="GET", headers=None, params=None, formdata=None, proxy=None, callback="parse"):
        self.url = url # 请求的url
        self.method = method    # 请求方法
        self.headers = headers  # 请求报头
        self.params = params    # 查询字符串
        self.formdata = formdata    # 表单数据
        self.proxy = proxy # 代理信息 {"http" : "http://ip:port"}
        self.callback = callback

