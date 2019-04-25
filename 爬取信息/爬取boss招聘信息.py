# 爬取招聘信息和本地保存
import requests
from bs4 import BeautifulSoup
import pandas as pd
import lxml

def webSpider():
    r = requests.get(url, headers=header)
    if r.status_code == 200:
        print('请求成功')
        r.encoding = 'utf-8'
        return r.text
    else:
        print('状态码不是200，请检查')

def htmlExtract(html):
    company_list=[]
    position_list = []
    salary_list = []

    soup = BeautifulSoup(html, 'html.parser')
    company_name = soup.find_all('h3',class_='name')
    for i in company_name:
        print(i.text.strip())  # strip()去掉字符串前后空格，不用去掉字符串中间空格
        company_list.append(i.text.strip())

    position_link = soup.find_all('div',class_='job-title')
    for i in position_link:
        print(i.text.strip())  # strip()去掉字符串前后空格，不用去掉字符串中间空格
        position_list.append(i.text.strip())

    salary = soup.find_all('span', class_='red')
    for i in salary:
        print(i.text.strip())  # strip()去掉字符串前后空格，不用去掉字符串中间空格
        salary_list.append(i.text.strip())

    columns = {'company':company_list, 'position':position_list, 'salary':salary_list}
    df = pd.DataFrame.from_dict(columns,orient='index') #数列保证相同
    df.to_csv('招聘信息.csv', index=False, encoding='utf_8_sig')


if __name__ == '__main__':
    url = 'https://www.zhipin.com/job_detail/?query=python&city=101200100&industry=&position='
    header = {
        'User-Agent': 'Mozilla/5.0(Windows NT 10.0; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
    }
    html = webSpider()
    txt = htmlExtract(html)
