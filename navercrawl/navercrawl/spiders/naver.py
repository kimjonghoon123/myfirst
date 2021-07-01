# -*- coding: utf-8 -*-
import scrapy
from navercrawl.items import NavercrawlItem
from navercrawl.pipelines import NavercrawlPipeline
import dload
import os
class NaverSpider(scrapy.Spider):
    img_floder ='./img'
    name = 'naver'
    allowed_domains = ['https://www.naver.com/']
    start_urls = ['http://https://www.naver.com//']

    def parse(self, response):
        item = NavercrawlItem()
        titles = response.xpath('//*[@id="NM_NEWSSTAND_DEFAULT_THUMB"]/div/div/div/div/div/a/img/@alt').getall()
        imgsrcs = response.xpath('//*[@id="NM_NEWSSTAND_DEFAULT_THUMB"]/div/div/div/div/div/a/img/@src').getall()
        for a in titles:
            item['title'] = a
        i=1
        for b in imgsrcs:
            imgsrc = b

            item['files'] = dload.save(imgsrc,f'./img/{i}.jpg')
            i+=1


        yield item