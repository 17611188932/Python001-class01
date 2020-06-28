
from fake_useragent import UserAgent
from scrapy.selector import Selector
import requests

ua = UserAgent(verify_ssl = False)
def get_one_page(url):

        useragent = ua.random
        headers = {
        "User-Agent": useragent
        }
        response = requests.get(url, headers = headers)
        print(response.text)


def parse_detail(url_text):

    film_name = Selector(text=url_text).xpath('//p[@class="name"]/text()')
    #film_gener = Selector(text=url_text).xpath()
    #plan_time = Selector(text=url_text).xpath()
    print(film_name)
    #print(plan_time)
    #print(film_gener)

url = 'https://maoyan.com/board/4'
url_text = get_one_page(url)
parse_detail(url_text)