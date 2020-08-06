#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
import hashlib
import time
from tkinter.filedialog import askopenfilenames
import mycsv
import codecs
import os
import pandas as pd
import threading
import json

class Dest_Data():
    def __init__(self):
        self.filenames = []
        self.cur_dir = os.getcwd()
        self.src_dir = self.cur_dir + "\\src\\"
        self.dst_dir = self.cur_dir + "\\dst\\"
        self.sheet_name = self.read_sheet_config_name()

    def read_sheet_config_name(self):
        try:
            if os.path.exists("sheet_config.json"):
                fd = open("sheet_config.json")
                login = fd.read()
                fd.close()
                jdict = json.loads(login)
                return jdict
        except Exception as e:
            return None

    def get_sheet_name(self, index):
        try:
            return self.sheet_name[str(index)]
        except Exception as e:
            return str(index)

    #功能函数
    def select_file(self):
        self.filenames = self.file_name(self.src_dir)

    def remove_dst_file(self):
        dstfile = self.file_name(self.dst_dir, '.xlsx')
        for item in dstfile:
            os.remove(item)

    def deal_file(self, filename, foldername):
        try:
            with open(filename, 'r', encoding='utf8') as f:  # 打开xls文件
                reader = mycsv.reader(f)
                result = list(reader)
                for index in range(1, len(result)):
                    tempfile = self.dst_dir+str(foldername)+"_"+result[index][2] + '.csv'
                    exist = os.path.exists(tempfile)
                    with open(tempfile, 'a', encoding='utf8', newline='') as wrfile:
                        w = mycsv.writer(wrfile)
                        if not exist:
                            w.writerow(result[0])
                        w.writerow(result[index])
        except:
            pass

    def generate_file(self):
        self.select_file()
        if 0 != len(self.filenames):
            for index in range(len(self.filenames)):
                self.deal_file(self.filenames[index], index)
            self.merge_file()

    @staticmethod
    def file_name(self, file_dir, filetype='.csv'):
        L = []
        for root, dirs, files in os.walk(file_dir, False):
            for file in files:
                if os.path.splitext(file)[1] == filetype:
                    L.append(root+file)
        return L

    @staticmethod
    def get_file(self, allfile):
        L = []
        for item in allfile:
            if len(L) == 0:
                L.append(item)
            elif L[0][-20:] == item[-20:]:
                L.append(item)
        return L

    def merge_file(self):
        while True:
            allfile = self.file_name(self.dst_dir)
            if 0 == len(allfile):
                break
            destfile = self.get_file(allfile)
            if 0 == len(destfile):
                break

            writer = pd.ExcelWriter(self.dst_dir+destfile[0][-20:-4]+'.xlsx')
            for index in range(len(destfile)):
                data1 = pd.read_csv(destfile[index], encoding="utf8")
                data1.to_excel(writer, sheet_name='0'+str(index), uuindex=False)
                os.remove(destfile[index])
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
    ZMJ_PORTAL.remove_dst_file()
    time.sleep(1)
    ZMJ_PORTAL.start_task()


if __name__ == '__main__':
	main()