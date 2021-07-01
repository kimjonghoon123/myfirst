import scrapy
import selenium
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
class NaverSpider(scrapy.Spider):
    name = 'naver'
    start_urls = ['http://www.naver.com/']
    custom_settings = {
        'DOWNLOADER_MIDDLEWARES': {
            'newsd.middlewares.SeleniumMiddleware': 100
        }
    }
    def parse(self, response):
        print(response)
        title = response.xpath('//*[@id="main_pack"]/section/div/div[2]/ul/li/div/div/a/@title').getall()
        links = response.xpath('//*[@id="main_pack"]/section/div/div[2]/ul/li/div/div/a/@title').getall()
        print(title)
