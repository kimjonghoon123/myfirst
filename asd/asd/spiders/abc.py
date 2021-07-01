import scrapy

class AbcSpider(scrapy.Spider):
    name = 'abc'
    start_urls = ['https://www.google.com/search?q=%ED%95%AD%EB%A7%8C&tbs=qdr:w&tbm=vid&sxsrf=ALeKk033TPCkQ4MugOASPftzfHLqEuRPlg:1624438920113&tbas=0&source=lnt&sa=X&ved=2ahUKEwjCiqvGsq3xAhVi7XMBHfEZADwQpwV6BAgBED8&biw=1197&bih=1158&dpr=0.8']



    def parse(self, response):

        titles = response.css('div.yuRUbf > a')
        print(titles)





