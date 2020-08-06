import requests
from requests.exceptions import RequestException
import re
import json
from multiprocessing import Pool

def get_one_page(url, headers):
   try:
        requests.adapters.DEFAULT_RETRIES = 5
        s = requests.session()
        s.keep_alive = False
        response = requests.get(url, headers=headers)
        response.encoding = 'utf-8'
        if response.status_code == 200:
            return response.text
        return None
   except RequestException as e:
        print(e)
        return None


def parse_one_page(html):
# 提取网页信息的正则表达式
    pattern = re.compile('<dd>.*?board-index.*?>(\d*)</i>.*?data-src="(.*?)".*?name"><a'
                         +'.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)(/p)'
                         +'.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>',re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {
            'index': item[0],
            'image': item[1],
            'title': item[2],
            'actor': item[3].strip()[3:],
            'time': item[4].strip()[5:len(item[4].strip())-1],
            'score': item[6]+item[7]
        }


# 写入result.txt文件中
def write_to_file(content):
    with open('result.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content,ensure_ascii=False) + '\n')
        f.close()

'''
def main():
    # 猫眼电影爬取需添加headers，从用户角度访问
    url = 'https://maoyan.com/board/4?offset=0'
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    cookies = 'uuid_n_v=v1; uuid=CF7EDAD000FB11EA948A1D596F2586CC860E9EDDF53E4207B1F54235B604914C; _csrf=d3cb3e30c02ea4a3d8aa5f01b01fca0e0681ce33dc9cad39ec500ee57488e256; _lxsdk_cuid=16e436c5d07c8-0b009b46405dc2-54123310-100200-16e436c5d07c8; _lxsdk=CF7EDAD000FB11EA948A1D596F2586CC860E9EDDF53E4207B1F54235B604914C; __mta=244766650.1573089205708.1573098217779.1573098223039.23'
    # headers = {'User-Agent': user_agent, 'Cookies': cookies}
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'
    cookies = 'uuid_n_v=v1; uuid=CF7EDAD000FB11EA948A1D596F2586CC860E9EDDF53E4207B1F54235B604914C; _csrf=d3cb3e30c02ea4a3d8aa5f01b01fca0e0681ce33dc9cad39ec500ee57488e256; _lxsdk_cuid=16e436c5d07c8-0b009b46405dc2-54123310-100200-16e436c5d07c8; _lxsdk=CF7EDAD000FB11EA948A1D596F2586CC860E9EDDF53E4207B1F54235B604914C; __mta=244766650.1573089205708.1573098217779.1573098223039.23'
    headers = {'User-Agent': user_agent,
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
               'Sec - Fetch - User': '?1',
               'Sec - Fetch - Site': 'none',
               'Sec - Fetch - Mode': 'navigate',
               'Accept - Encoding': 'gzip, deflate, br',
               'Accept - Language': 'zh - CN, zh;',
               'Cookies': cookies}
    # headers = {'User-Agent': user_agent}
    html = get_one_page(url, headers)
    if html.__eq__(None):
        print("error")
        return
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)


if __name__ == '__main__':
    main()
'''

def main(offset):
    url = 'https://maoyan.com/board/4?offset='+str(offset)
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = {'User-Agent': user_agent, 'Connection': 'close'}
    html = get_one_page(url, headers)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)


if __name__ == '__main__':
    p = Pool()
    p.map(main, [i*10 for i in range(10)])

