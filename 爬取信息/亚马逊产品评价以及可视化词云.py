import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

def bookSpider():
    r = requests.get(url,headers=header)
    r.encoding='utf-8'
    #print(r.text)

    soup = BeautifulSoup(r.text,'lxml')
    review = soup.find_all('span',class_=True)
    print(review)
    content=''
    for i in review:
        print(i.text.strip())
        content=''.join(i.text.strip())
    #print(content)
    return content

def wordCloud(txt):
    wc = WordCloud(
        background_color='white', #设置背景颜色
        max_font_size=80,  #设置字体最大值
        max_words=200,
        scale=3,  #设置清晰度
        stopwords=STOPWORDS
    ).generate(txt)
    plt.figure()
    plt.imshow(wc,interpolation='bilinear')
    plt.axis('off')
    plt.show()

if __name__=='__main__':
    url='https://www.amazon.com/Head-First-Python-Brain-Friendly-Guide/dp/1491919531/ref=sr_1_1?crid=2R0IA9IHE0BWE&keywords=head+first+python&qid=1556075661&s=gateway&sprefix=Head+firs%2Caps%2C406&sr=8-1'
    header = {
        'User-Agent': 'Mozilla/5.0(Windows NT 10.0; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
    }
    text = bookSpider()
    wordCloud(text)
