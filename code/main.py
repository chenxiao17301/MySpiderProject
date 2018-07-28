#coding:utf-8

from scrapy_plus.core.engine import Engine

# # 导入所有爬虫类
#from spiders.baidu import BaiduSpider
# from spiders.douban import DoubanSpider

# # 导入所有管道类
# from pipelines import BaiduPipeline1, BaiduPipeline2, DoubanPipeline1, DoubanPipeline2

# # 导入所有中间件类
# from middlewares import SpiderMiddleware1, SpiderMiddleware2, DownloaderMiddleware1, DownloaderMiddleware2


# import settings

# import importlib

def main():
    # 构建自定义的Spider对象
    # baidu_spider = BaiduSpider()
    # douban_spider = DoubanSpider()
    # # 将对象做为参数传给Engine


    #getattr(对象，属性)
    #getattr(文件绝对路径，文件里的类)



    # 构建需要执行的多个爬虫的字典
    # spiders = {
    #     BaiduSpider.name : BaiduSpider(),
    #     DoubanSpider.name : DoubanSpider()
    # }

    # # 自定义管道
    # pipelines = [
    #     BaiduPipeline1(),
    #     BaiduPipeline2(),
    #     DoubanPipeline1(),
    #     DoubanPipeline2(),
    # ]

    # # 自定义爬虫中间件
    # spider_middlewares = [
    #     SpiderMiddleware1(),
    #     SpiderMiddleware2()
    # ]

    # # 自定义下载中间件
    # downloader_middlewares = [
    #     DownloaderMiddleware1(),
    #     DownloaderMiddleware2()
    # ]


    # engine = Engine(
    #     spiders = spiders,
    #     pipelines = pipelines,
    #     spider_mids = spider_middlewares,
    #     downloader_mids = downloader_middlewares
    # )


    engine = Engine()
    engine.start()


if __name__ == "__main__":
    main()
