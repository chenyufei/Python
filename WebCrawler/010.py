# -*- coding: cp936 -*-

import urllib3, urllib, sys, io
""" 

ʹ��GET�ڰٶ����������ϲ�ѯ 

������ʾ�������GET��,����������. 

"""

url = "http://www.baidu.com/s"

search = [('w', 'python')]

getString = url + "?" + str(search)  # �ؼ���ת��Ϊ�ַ���

req = urllib.Request(getString)  # �ύ�ַ���

fd = urllib.urlopen(req)  # ����ַ

baiduResponse = ""  # �õ��ٶȵĻ�Ӧ

while 1:

    data = fd.read(1024)  # ����

    if not len(data):
        break

    baiduResponse += data

fobj = open("baidu.html", 'w')  # ��baidu.html�ļ�������д��

fobj.write(baiduResponse)  # ��baidu.html�ļ�������д��

fobj.close()