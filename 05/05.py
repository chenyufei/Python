# -*- coding:utf-8 -*-
# The author is Sympathy
from bs4 import BeautifulSoup
import requests
import lxml
import csv
import bs4
import json
from lxml import etree

def chenyu():
    # --*--conding:utf-8 --*--
    # Author: Gonggong
    # 使用python爬取一个网页中表格的内容，并把抓取到的内容以json格式保存到文件中

    # 获取网页源代码
    r = requests.get('http://ipwhois.cnnic.cn/bns/query/Query/ipwhoisQuery.do?queryOption=ipv4&txtquery=8.8.8.8')

    # 使用xpath对爬取的源代码进行处理
    dom_tree = etree.HTML(r.content)
    links = dom_tree.xpath("/html/body/center[1]/table[1]/tr/td/font")

    # 取出links的单行、双行的数据
    res1 = [i.text for i in links[::2]]
    res2 = [i.text for i in links[1::2]]

    # 把两行数据组合成在一起
    result = tuple(zip(res1, res2))

    # 使用json格式保存到文件中
    json.dump(result, open('E:/chenyufei/xpath_get.txt', 'w'), ensure_ascii=False)


# 用于抓取湖大硕士生招生初试线表格数据
def check_link(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print('无法连接服务器')


def get_contents(ulist, rurl):
    soup = BeautifulSoup(rurl, 'lxml')
    trs = soup.find_all('tr')
    for tr in trs:
        ui = []
        for td in tr:
            ui.append(td.string)
        ulist.append(ui)


def save_contents(urlist):
    with open("E:/chenyufei/2018年湖大初试成绩线.csv", 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['2018湖大初试成绩'])
        for i in range(len(urlist)):
            for p in range(1, 10):
                urlist[i].append(' ')
            if i not in [0, 1, 15, 32, 34, 35, 36, 37]:
                for p in range(2):
                    urlist[i].insert(0, ' ')
            elif i in [32, 34, 36]:
                for p in range(4):
                    urlist[i].insert(0, ' ')
            elif i in [35, 37]:
                for p in range(6):
                    urlist[i].insert(0, ' ')
            writer.writerow([urlist[i][1], urlist[i][3], urlist[i][5], urlist[i][7], urlist[i][9], urlist[i][11],
                             urlist[i][13]])


def main():
    urli = []
    #  url = "http://gra.hnu.edu.cn/info/1075/4129.htm"
    url = "http://gra.hnu.edu.cn/index/xwxx.htm"
    chenyu()
    rs = check_link(url)
    get_contents(urli, rs)
    # save_contents(urli)


if __name__ == '__main__':
    main()
