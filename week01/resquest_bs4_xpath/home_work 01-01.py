
import requests
from requests.exceptions import RequestException
from bs4 import BeautifulSoup as soup
from urllib import parse
import lxml.etree
import csv
import time

#获取主页面text
def get_one_page(url):
    try:
        headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
        }
        response = requests.get(url, headers = headers)
        #print(response.text)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

#通过主页面解析出每个电影的独立网址，并返回
def get_url(html):
    urls = [] #空列表,存放网址后缀
    url_join = [] #空列表，存放拼接后的网址
    soup_info = soup(html,'html.parser')
    #print(soup_info)
    for tags in soup_info.find_all(name = 'div',attrs={'class':'movie-item-info'}):
        for atag in tags.find_all(name = 'a',):
            urls.append(atag.get('href'))  #网址增加到列表内
    #print(urls)
    # 网址拼接
    url_sum = 'https://maoyan.com/'
    for url in urls:
        url_join.append(parse.urljoin(url_sum,url))
    return url_join

#获取每个电影详细信息，包括名称、类型、上映时间
def get_every_page(url_join):

        headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
        }
        #print(url_join)
        for url_one in url_join:
            response = requests.get(url_one, headers = headers)

            selector = lxml.etree.HTML(response.text)
            film_name = selector.xpath('/html/body/div[3]/div/div[2]/div[1]/h1/text()')
            #print(f'电影名称: {film_name}')
            film_gener = selector.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[1]/a/text()')
            #print(f'电影类型：{film_gener}')
            paln_data = selector.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[3]/text()')
            #print(f'上映时间：{paln_data}')

            movie_list = [film_name, film_gener, paln_data]
            #print(movie_list)
            with open('movie.csv','a') as csvfile:
                writer = csv.writer(csvfile,)
                writer.writerow([film_name ,film_gener,paln_data])
            time.sleep(3)

def main():
    url = 'https://maoyan.com/board/4'
    html = get_one_page(url)
    text = get_url(html)
    get_every_page(text)

main()