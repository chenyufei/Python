#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
from bs4 import BeautifulSoup
import re
import time
import threading

word = []


def getEnglishWord(num):
    try:
        base_url = 'http://www.kuakao.com/english/ch/39%d.html'% num
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36'}
        r = requests.get(base_url, headers=headers)
        r.encoding = r.apparent_encoding
        soup = BeautifulSoup(r.content, 'lxml')
        # print(soup)
        # artTxt = soup.find('div', class_='artTxt').get_text()
        artTxt = soup.find('div', class_='artTxt')
        regex = r'</?p>'
        for txt in artTxt:
            if str(txt).startswith("<p>"):
                wd = re.sub(regex, "", str(txt), re.I).strip()
                if re.match(r'\d', wd):
                    wd = re.sub(r'\d', "", wd).strip()
                    print(wd)
                    word.append(wd)
    except Exception as e:
        print(e)


def englishWord():
    for index in range(183, 249):
        getEnglishWord(index)
        time.sleep(1)


if __name__ == '__main__':
    word_thread = threading.Thread(target=englishWord)
    word_thread.setDaemon(True)
    word_thread.start()
    word_thread.join()

    with open('word.txt', 'w', encoding='utf-8') as f:
        for wd in word:
            f.write(wd+"\n")
        f.write('\n')
        f.close()

