#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
import hashlib
import time
from tkinter.filedialog import askopenfilenames
import csv
import codecs
import os
import pandas as pd
import threading


LOG_LINE_NUM = 0


class MY_GUI():
    def __init__(self,init_window_name):
        self.init_window_name = init_window_name
        self.filenames = []

    #设置窗口
    def set_init_window(self):
        self.init_window_name.title("GSP处理工具_v1.0")           #窗口名
        #self.init_window_name.geometry('320x160+10+10')                         #290 160为窗口大小，+10 +10 定义窗口弹出时的默认展示位置
        self.init_window_name.geometry('1068x681+10+10')
        #self.init_window_name["bg"] = "pink"                                    #窗口背景色，其他背景色见：blog.csdn.net/chl0000/article/details/7657887
        #self.init_window_name.attributes("-alpha",0.9)                          #虚化，值越小虚化程度越高
        #标签
        self.select_file_button = Button(self.init_window_name, text="选择文件", bg="lightblue", width=10,command=self.select_file)  # 调用内部方法  加()为直接调用
        self.select_file_button.grid(row=0, column=3)

        self.init_data_label = Label(self.init_window_name, text="待处理文件")
        self.init_data_label.grid(row=1, column=0)

        self.result_data_label = Label(self.init_window_name, text="输出结果")
        self.result_data_label.grid(row=0, column=12)
        self.log_label = Label(self.init_window_name, text="日志")
        self.log_label.grid(row=12, column=0)
        #文本框
        self.init_data_Text = Text(self.init_window_name, width=67, height=35)  #原始数据录入框
        self.init_data_Text.grid(row=2, column=0, rowspan=10, columnspan=10)

        self.result_data_Text = Text(self.init_window_name, width=70, height=49)  #处理结果展示
        self.result_data_Text.grid(row=1, column=12, rowspan=15, columnspan=10)

        self.log_data_Text = Text(self.init_window_name, width=66, height=9)  # 日志框
        self.log_data_Text.grid(row=13, column=0, columnspan=10)
        #按钮
        self.str_trans_to_md5_button = Button(self.init_window_name, text="处理", bg="lightblue", width=10,command=self.start_task)  # 调用内部方法  加()为直接调用
        self.str_trans_to_md5_button.grid(row=4, column=11)

    #功能函数
    def select_file(self):
        self.filenames = askopenfilenames()
        self.init_data_Text.delete(1.0, END)
        if len(self.filenames) != 0:
            string_filename = ""
            self.record_file("您选择的文件是：")
            for i in range(0, len(self.filenames)):
                string_filename += str(self.filenames[i]) + "\r\n"
            self.record_file(string_filename)
        else:
            self.write_log_to_Text("您没有选择任何文件")

    def deal_file(self, filename, foldername):
        print(filename)
        try:
            with open(filename, 'r', encoding='utf8') as f:  # 打开xls文件
                reader = csv.reader(f,)
                result = list(reader)
                print(len(result))
                for index in range(1, len(result)):
                    exist = os.path.exists(str(foldername)+"_"+result[index][2] + '.csv')
                    with open(str(foldername)+"_"+result[index][2] + '.csv', 'a', encoding='utf8', newline='') as wrfile:
                        w = csv.writer(wrfile)
                        if not exist:
                            w.writerow(result[0])
                        w.writerow(result[index])
            self.result_data_Text.insert(END, "处理文件:" + filename + " 成功\r\n")
        except:
            self.result_data_Text.insert(END, "处理文件:"+filename+" 失败\r\n")

    def generate_file(self):
        self.result_data_Text.delete(1.0, END)
        for index in range(len(self.filenames)):
            self.deal_file(self.filenames[index], index)
            time.sleep(2)
        self.merge_file()

    def file_name(self, file_dir):
        L = []
        for root, dirs, files in os.walk(file_dir):
            for file in files:
                if os.path.splitext(file)[1] == '.csv':
                    L.append(file)
        return L

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
            allfile = self.file_name(os.getcwd())
            if 0 == len(allfile):
                break
            destfile = self.get_file(allfile)
            if 0 == len(destfile):
                break

            writer = pd.ExcelWriter(destfile[0][-20:-4]+'.xlsx')
            for index in range(len(destfile)):
                data1 = pd.read_csv(destfile[index], encoding="utf8",error_bad_lines=False)
                data1.to_excel(writer, sheet_name='0'+str(index),index=False)
                os.remove(destfile[index])
            writer.save()
    def start_task(self):
        checkthread = threading.Thread(target=self.generate_file)
        checkthread.setDaemon(True)
        checkthread.start()

    def str_trans_to_md5(self):
        src = self.init_data_Text.get(1.0, END).strip().replace("\n", "").encode()
        #print("src =",src)
        if src:
            try:
                myMd5 = hashlib.md5()
                myMd5.update(src)
                myMd5_Digest = myMd5.hexdigest()
                #print(myMd5_Digest)
                #输出到界面
                self.result_data_Text.delete(1.0,END)
                self.result_data_Text.insert(1.0,myMd5_Digest)
                self.write_log_to_Text("INFO:str_trans_to_md5 success")
            except:
                self.result_data_Text.delete(1.0,END)
                self.result_data_Text.insert(1.0,"字符串转MD5失败")
        else:
            self.write_log_to_Text("ERROR:str_trans_to_md5 failed")


    #获取当前时间
    def get_current_time(self):
        current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        return current_time

    def record_file(self, filename):
        self.init_data_Text.insert(END, filename+"\r\n")


    #日志动态打印
    def write_log_to_Text(self,logmsg):
        global LOG_LINE_NUM
        current_time = self.get_current_time()
        logmsg_in = str(current_time) + " " + str(logmsg) + "\r\n"      #换行
        if LOG_LINE_NUM <= 7:
            self.log_data_Text.insert(END, logmsg_in)
            LOG_LINE_NUM = LOG_LINE_NUM + 1
        else:
            self.log_data_Text.delete(1.0,2.0)
            self.log_data_Text.insert(END, logmsg_in)


def gui_start():
    init_window = Tk()              #实例化出一个父窗口
    ZMJ_PORTAL = MY_GUI(init_window)
    # 设置根窗口默认属性
    ZMJ_PORTAL.set_init_window()

    init_window.mainloop()          #父窗口进入事件循环，可以理解为保持窗口运行，否则界面不展示


gui_start()
