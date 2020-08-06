#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib
import time
import csv
import codecs
import os
import pandas as pd
import threading
import json

class Dest_Data():
    def __init__(self):
        self.foldnames = []
        self.cur_dir = os.getcwd()
        self.src_dir = self.cur_dir + "\\src\\"
        self.dst_dir = self.cur_dir + "\\dst\\"
        self.deveuis = []
        self.deveui_file = self.cur_dir +"\\deveui\\deveui.txt"

    def readtext(self,filename):
        lines = []
        with open(filename, 'r') as file_to_read:
            while True:
                line = file_to_read.readline()
                if not line:
                    break
                line = line.strip('\n')
                lines.append(line)
        return lines

    def get_deveui(self):
        self.deveuis = self.readtext(self.deveui_file)

    def get_fold(self):
        for root, dirs, files in os.walk(self.src_dir):
            self.foldnames = dirs
            print('sub_dirs:', self.foldnames)
            break

    #功能函数
    def generate_temp_file(self):
        for item in self.foldnames:
            cur_dir = self.src_dir+item+"\\"
            os.chdir(cur_dir)
            filenames = self.file_name(cur_dir)
            count = 0
            for temp in filenames:
                print(temp)
                count += self.deal_file(temp, item)
            print(item +":"+str(count))

    def remove_dst_file(self, filetype='.csv'):
        dstfile = self.file_name(self.dst_dir, filetype)
        for item in dstfile:
            os.remove(item)

    def deal_file(self, filename, foldername):
        try:
            with open(filename, 'r', encoding='utf8') as f:  # 打开xls文件
                reader = csv.reader(f)
                result = list(reader)
                count = 0
                for index in range(1, len(result)):
                    deveui = result[index][2][-16:]
                    if self.deveuis.count(deveui) == 0:
                        continue

                    tempfile = self.dst_dir+str(foldername)+"_"+result[index][2] + '.csv'
                    exist = os.path.exists(tempfile)
                    with open(tempfile, 'a', encoding='utf8', newline='') as wrfile:
                        w = csv.writer(wrfile)
                        if not exist:
                            w.writerow(result[0])
                            count = count + 1
                        w.writerow(result[index])
                return count
        except:
            print("处理文件:"+filename + " 异常")
            return 0

    def generate_file(self):
        self.get_fold()  # 获取子目
        self.get_deveui()  # 获取需要生成的deveui列表
        self.generate_temp_file() # 根据获取的子目录获取子目录下的文件
        self.merge_file()

    @staticmethod
    def file_name(file_dir, filetype='.csv'):
        L = []
        for root, dirs, files in os.walk(file_dir, False):
            for file in files:
                if os.path.splitext(file)[1] == filetype:
                    L.append(root+file)
        return L

    @staticmethod
    def get_file(allfile):
        L = []
        for item in allfile:
            if len(L) == 0:
                L.append(item)
            elif L[0][-20:] == item[-20:]:
                L.append(item)
        return L

    def merge_file(self):
        allfile = self.file_name(self.dst_dir)
        if 0 == len(allfile):
            return
        for item in allfile:
            bExit = os.path.exists(self.dst_dir + item[-20:-4] + '.xlsx')
            #writemode = 'w' if bExit else  'a'
            writer = pd.ExcelWriter(self.dst_dir + item[-20:-4] + '.xlsx',mode='a' if bExit else 'w')
            data1 = pd.read_csv(item, encoding="utf8")
            filename = os.path.basename(item)
            name = filename.split("_")[0]
            data1.to_excel(writer, sheet_name=name, index=False)
            writer.save()

    def start_task(self):
        checkthread = threading.Thread(target=self.generate_file)
        checkthread.setDaemon(True)
        checkthread.start()
        checkthread.join()


    #获取当前时间
    def get_current_time(self):
        current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        return current_time

def main():
    ZMJ_PORTAL = Dest_Data()
    ZMJ_PORTAL.remove_dst_file('.csv')
    ZMJ_PORTAL.remove_dst_file('.xlsx')
    time.sleep(1)
    print("开始处理")
    ZMJ_PORTAL.start_task()
    ZMJ_PORTAL.remove_dst_file('.csv')
    print("处理结束")


if __name__ == '__main__':
	main()