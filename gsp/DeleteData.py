import csv
import time
import os

dstpath = input("请输入目录:")
os.chdir(dstpath)
dstfile = input("请输入目标文件")
time.sleep(2)
print('正在处理............')
with open(dstfile, 'r',encoding='utf8') as fin, open("dst"+dstfile, 'w', newline='',encoding='utf8') as fout:
    reader = csv.reader(fin, skipinitialspace=True)
    writer = csv.writer(fout, delimiter=',')
    writer.writerow(next(reader))
    for index in reader:
        if str(index[-1]).startswith("14"):
            pass
        else:
            writer.writerow(index)
print('写入完毕！')
print('10秒钟自动关闭程序！')
