import scrapy


class KjhtubeSpider(scrapy.Spider):
    name = 'kjhtube'
    allowed_domains = ['www.youtube.com']
    start_urls = ['http://www.youtube.com/']

    def parse(self, response):
        pass


//*[@id="video-title"]