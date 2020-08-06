import requests
from requests.exceptions import RequestException
import re
import json
from lxml import etree
from multiprocessing import Pool
from bs4 import BeautifulSoup


def get_one_page(url, headers):
   try:
        response = requests.get(url, headers=headers)
        response.encoding = 'utf-8'
        # print(response)
        if response.status_code == 200:
            return response.text
        return None
   except RequestException as e:
       print(e)
       return None


def parse_one_page(html):
# 提取网页信息的正则表达式
    '''
    pattern = re.compile('<dd>.*?board-index.*?>(\d*)</i>.*?data-src="(.*?)".*?name"><a'
                         +'.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)(/p)'
                         +'.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>',re.S)
    '''
    pattern = re.compile('"objURL":"(.*?).jpeg"', re.S)
    patterncore = re.compile('<dd>.*?title="(.*?)"></a>.*?channel-detail-orange">.*?integer">(.*?)</i>.*?fraction">(.*?)</i></div>', re.S)
    items = re.findall(pattern, html)
    # print(items)
    for item in items:
        yield {
            'imageurl': item
        }



# 写入result.txt文件中
def write_to_file(content):
    with open('result.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content,ensure_ascii=False) + '\n')
        f.close()


def main():
    #url = 'https://www.baidu.com/'
    url = 'http://image.baidu.com/search/index?ct=201326592&cl=2&st=-1&lm=-1&nc=1&ie=utf-8&tn=baiduimage&ipn=r&rps=1&pv=&fm=rs2&word=%E5%A3%81%E7%BA%B8%E6%83%85%E4%BE%A3&oriquery=%E5%A3%81%E7%BA%B8&ofr=%E5%A3%81%E7%BA%B8&sensitive=0'
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'
    cookies = 'uuid_n_v=v1; uuid=CF7EDAD000FB11EA948A1D596F2586CC860E9EDDF53E4207B1F54235B604914C; _csrf=d3cb3e30c02ea4a3d8aa5f01b01fca0e0681ce33dc9cad39ec500ee57488e256; _lxsdk_cuid=16e436c5d07c8-0b009b46405dc2-54123310-100200-16e436c5d07c8; _lxsdk=CF7EDAD000FB11EA948A1D596F2586CC860E9EDDF53E4207B1F54235B604914C; __mta=244766650.1573089205708.1573098217779.1573098223039.23'
    headers = {
               'Referrer Policy': 'no-referrer-when-downgrade',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
               'Sec-Fetch-User': '?1',
               'Sec-Fetch-Site': 'none',
               'Sec-Fetch-Mode': 'navigate',
               'Accept-Encoding': 'gzip, deflate, br',
               'Accept-Language': 'zh-CN, zh;q=0.9',
               'Upgrade_insecure-Requests':str(1),
               'Connection':'keep-alive',
               'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
               }
    html = get_one_page(url, headers)
    # print(html)
    # soup = BeautifulSoup(html, 'lxml')
    # ddTag = soup.find_all('dd')
    # print(ddTag)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)


if __name__ == '__main__':
    main()
