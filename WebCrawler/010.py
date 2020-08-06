# -*- coding: cp936 -*-

import urllib3, urllib, sys, io
""" 

使用GET在百度搜索引擎上查询 

此例演示如何生成GET串,并进行请求. 

"""

url = "http://www.baidu.com/s"

search = [('w', 'python')]

getString = url + "?" + str(search)  # 关键词转化为字符串

req = urllib.Request(getString)  # 提交字符串

fd = urllib.urlopen(req)  # 打开网址

baiduResponse = ""  # 得到百度的回应

while 1:

    data = fd.read(1024)  # 遍历

    if not len(data):
        break

    baiduResponse += data

fobj = open("baidu.html", 'w')  # 打开baidu.html文件，用于写入

fobj.write(baiduResponse)  # 打开baidu.html文件，用于写入

fobj.close()