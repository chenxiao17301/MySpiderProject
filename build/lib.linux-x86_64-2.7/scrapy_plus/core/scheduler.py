#coding:utf-8

# 根据异常判断，导入适合解释器环境的队列类
# try:
#     from Queue import Queue
# except:
#     from queue import Queue

# 根据解释器环境，判断是py2/py3，并导入对应的队列类
from six.moves.queue import Queue

class Scheduler(object):
    def __init__(self):
        self.queue = Queue()
        self._filter_set = set()


    def add_request(self, request):
        if self._filter_request(request):
            self._filter_set.add(request.url)
            self.queue.put(request)


    def get_request(self):
        try:
            return self.queue.get(False)
        except:
            return False


    def _filter_request(self, request):
        """
            请求去重，并返回判断结果
        """
        # 如果请求的url地址不再去重集合中，那么返回True，表示允许添加到请求队列中
        if request.url not in self._filter_set:
            return True
        else:
            # 否则，表示重复， 不允许添加
            return False
