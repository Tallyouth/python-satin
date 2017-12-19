import requests
from urllib import request
from urllib import error
from bs4 import BeautifulSoup
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
def get_page(url):
    try:
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
        headers = {'User-Agent': user_agent}
        req = request.Request(url, headers=headers)
        response = request.urlopen(req).read()
        response = response.decode('utf-8')
        return response
    except error.URLError as e:
        print(e.reason)
def get_duanzi(html):
    response = get_page(html)
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(response, 'html.parser')
    item = []
    long = soup.select('div[class="article block untagged mb15 typs_long"]')
    hot = soup.select('div[class="article block untagged mb15 typs_hot"]')
    old = soup.select('div[class="article block untagged mb15 typs_old"]')
    for one in long:
        item.append(one)
    for two in hot:
        item.append(two)
    for three in old:
        item.append(three)
    for news in item:
        name = news.select('h2')[0].text
        body = news.select('span')[0].text
        comment = news.select('i[class="number"]')[0].text
        print('作者是：', name)
        print(body)
        print('评论数是：', comment)
    main()
def main():
    page_number = input('请输入你想看第几页')
    print('正在加载第{}页'.format(page_number))
    url = 'https://www.qiushibaike.com/hot/page/{}/'.format(page_number)
    get_duanzi(url)
if __name__ == '__main__':
    main()
