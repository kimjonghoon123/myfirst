import scrapy


class TitlecrawlSpider(scrapy.Spider):
    name = 'titlecrawl'
    allowed_domains = ['https://search.naver.com/search.naver?where=news']
    start_urls = ['http://https://search.naver.com/search.naver?where=news/']

    def parse(self, response):
        pass
