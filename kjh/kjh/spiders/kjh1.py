# -*- coding: utf-8 -*-
import scrapy
from kjh.items import KjhItem

class Kjh1Spider(scrapy.Spider):
    name = 'kjh1'
    start_urls = ['https://www.naver.com/']
    custom_settings= {
        'ITEM_PIPELINES' : {
        'scrapy.pipelines.images.ImagesPipeline': 1,
        }
    }
    def parse(self, response):
        srcs = response.xpath('//*[@id="NM_NEWSSTAND_DEFAULT_THUMB"]/div/div/div/div/div/a/img')

        for elem in srcs:
            img_url = elem.xpath("@src").extract_first()
            print(img_url)
            yield {'image_urls': [img_url]}
