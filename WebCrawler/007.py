import requests
from requests.exceptions import RequestException
import re
import json
from multiprocessing import Pool


def get_one_page(url, headers):
   try:
        response = requests.get(url, headers=headers)
        response.encoding = 'utf-8'
        if response.status_code == 200:
            return response.text
        return None
   except RequestException as e:
        print(e)
        return None


def main():
    # 猫眼电影爬取需添加headers，从用户角度访问
    url = 'https://maoyan.com'
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'
    headers = {'User-Agent': user_agent}
    html = get_one_page(url, headers)
    pattern = re.compile('<span class="textcolor_.*?>(.*?)</span>', re.S)
    items = re.findall(pattern, html)
    print(items)

    pattern = re.compile('<span class=".*?ranking-.*?movie-name">(.*?)</span>', re.S)
    items = re.findall(pattern, html)
    print(items)

    #pattern = re.compile('<span class="ranking-movie-name">(.*?)</span>', re.S)
    #items = re.findall(pattern, html)
    #print(items)
    if len(html) == 0:
        print("error")
        return


if __name__ == '__main__':
    main()


