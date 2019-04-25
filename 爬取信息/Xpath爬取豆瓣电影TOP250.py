
import requests
from lxml import etree
import time  #降低爬取频率

movies = []

def moviesSpider():
    for i in range(0,250,25):
        url='https://movie.douban.com/top250?start='+str(i)+'&filter='
        header = {
            'User-Agent': 'Mozilla/5.0(Windows NT 10.0; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
        }

        r = requests.get(url,headers=header)  #也可添加Cookies信息
        r.encoding='utf-8'

        selector = etree.HTML(r.text)
        txt = selector.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div/div/a/span[1]/text()')
        print(txt)
        movies.extend(txt)
        time.sleep(3)

if __name__ == '__main__':
    moviesSpider()
    print(movies)