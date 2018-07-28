#coding:utf-8


# 覆盖了框架default_settings里的同名配置
DEFAULT_LOG_FILENAME = 'myspider.log'    # 默认日志文件名称


SPIDERS = [
    "spiders.baidu.BaiduSpider",
    "spiders.douban.DoubanSpider",
]


PIPELINES = [
    "pipelines.BaiduPipeline1",
    "pipelines.DoubanPipeline1",
]

SPIDER_MIDDLEWARES = [
    "middlewares.SpiderMiddleware1",
    "middlewares.SpiderMiddleware2"
]

DOWNLOADER_MIDDLEWARES = [
    "middlewares.DownloaderMiddleware1",
    "middlewares.DownloaderMiddleware2"
]

