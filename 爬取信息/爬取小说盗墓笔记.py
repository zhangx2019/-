# 盗墓笔记网址：https://www.taiuu.com/0/67/

import requests
import re

def novelSpider():
    with open('盗墓笔记.txt','a+') as f:
        for i in range(78215,78218):
            url = 'https://www.taiuu.com/0/67/'+ str(i) +'.html'
            r = requests.get(url,headers=header)
            if r.status_code == 200:
                print('请求成功!')
                r.encoding = 'gbk'
                # print(r.text)
                contents = re.findall('<div id="htmlContent".*上一章',r.text,re.S)

                for i in contents:
                    content = re.findall('[\u4e00-\u9fa5]',i) #提取中文表达式
                    print(''.join(content))
                    txt = ''.join(content)
                    f.write(txt+'\n')

if __name__ == '__main__':
    header = {
        'User-Agent': 'Mozilla/5.0(Windows NT 10.0; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
    }
    novelSpider()