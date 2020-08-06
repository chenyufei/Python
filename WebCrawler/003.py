#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
from bs4 import BeautifulSoup
import re
import time
import threading

try:
    base_url = 'http://ipwhois.cnnic.cn/bns/query/Query/ipwhoisQuery.do?queryOption=ipv4&txtquery=8.8.8.8'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36'}
    r = requests.get(base_url, headers=headers)
    r.encoding = r.apparent_encoding
    soup = BeautifulSoup(r.content, 'lxml')
    trTag = soup.find_all('tr')
    regex = r'</?tr>'
    trgroup = []
    for tr in trTag:
        td = re.sub(regex, "", str(tr), re.I).strip()
        if td.startswith('<td align="left" class="t_blue"><font size="2">') and td.endswith('</font></td>'):
            td = re.sub('<td align="left" class="t_blue"><font size="2">', "", td)
            td = re.sub('</font></td>', "", td).strip()
            trgroup.append(td)
    f = open("cnnic.txt", "w", encoding='utf-8')
    try:
        for t in trgroup:
            arr = t.splitlines()
            if len(arr) > 1:
                if arr[0].strip() != '':
                    print(arr[0] + arr[1])
                    f.write(arr[0] + arr[1] + '\n')
    except Exception as e:
        print(e)
    finally:
        f.close()
    print("====")
except Exception as e:
    print(e)
