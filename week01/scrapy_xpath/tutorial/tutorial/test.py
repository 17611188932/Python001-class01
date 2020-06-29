
from fake_useragent import UserAgent
from scrapy.selector import Selector
import requests
from scrapy import Selector
from urllib import parse
from urllib.parse import urljoin


base_url = 'http://maoyan.com'
file = 'D:\\maoyan.html'
with open(file,'r',encoding='utf-8') as object:
    body = object.read()
    #print(body)

selector = Selector(text=body)
content = selector.xpath('//div[@class="movie-item-info"]').getall()
for item in content[:10]:
    film_url = Selector(text=item).xpath('./descendant::a/@href').getall()
    url = base_url +film_url[0]
    print(url)

file_detail = 'D:\\maoyan_detail.html'
with open(file_detail,'r',encoding='utf-8') as object_detail:
    body = object_detail.read()
#selector = Selector(text=body)
film_name = Selector(text=body).xpath('//h1[@class="name"]/text()').getall()
film_gener = Selector(text=body).xpath('//ul/li[@class="ellipsis"]/a/text()').getall()
plan_time = Selector(text=body).xpath('//ul/li[3][@class="ellipsis"]/text()').getall()
print(film_name)
print(film_gener)
print(plan_time)
#film_name = Selector(text=tage).xpath('//h1[@class="name"]/text()').extract_first
#print(film_name)

import pymysql
db = pymysql.connect()





