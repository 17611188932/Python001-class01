# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from tutorial.items import TutorialItem            #导入itmes
from urllib.parse import urljoin
from fake_useragent import UserAgent
import time

class MoviesSpider(scrapy.Spider):
    name = 'movies'                                #项目名字
    allowed_domains = ['movies.maoyan.com']        #爬取的域名，如果爬取不是该域名下会被过滤
    start_urls = ['https://maoyan.com/board/4']    #spider爬取的url列表



    def start_requests(self):
        ua = UserAgent(verify_ssl=False)
        useragent = ua.random
        #Referer = 'https://maoyan.com'
        headers = {
            'User-Agent':useragent
         }
        url = 'https://maoyan.com/board/4'
        '''
        for i in range(0,10):
            if i == 0:
                url = url
                #print(url)
            else:
                url = f'https://maoyan.com/board/4?offset={ i * 10}'
                #print(url)
                time.sleep(3)
        '''
        yield scrapy.Request(url=url, callback=self.parse)

    # 解析返回的响应，提取数据、或者进一步处理
    def parse(self, response):
        print(response.text)
        item = []
        public_url = 'https://maoyan.com'
        link_list = Selector(text=response).xpath('//div[@class="movie-item-info"]/p[@class="name"]').extract
        print(link_list)
        for link in link_list:
            item = TutorialItem()
            movie_url = link.xpath('./a/@href').extract_first
            url = urljoin(public_url,movie_url)
            yield scrapy.Request(url=url, meta={'item': item}, callback=self.parse_detail)   #返回下一次的请求，也就是返回parse_detail

    #解析每个电影的详细信息、包括电影名、类型、上映时间
    def parse_detail(self,response):
        item = response.meta['item']
        film_name = Selector(response=response).xpath('//h1[@class="name"]/text()').extract_first
        target = Selector(response=response).xpath('//div[@class="movie-brief-container"]')
        film_gener = target.xpath('//ul/li[@class="ellipsis"]/a/text()').extract
        plan_time = target.xpath('//ul/li[3][@class="ellipsis"]/text()').extract_first
        item['film_name'] = film_name
        item['film_gener'] = film_gener
        item['plan_time'] = plan_time
        yield item