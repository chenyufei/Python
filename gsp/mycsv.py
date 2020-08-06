import glob
import time
import os

dstpath = input("请输入目录:")
os.chdir(dstpath)
print(os.getcwd())
csvx_list = glob.glob('*.csv')
print('总共发现%s个CSV文件' % len(csvx_list))
time.sleep(2)
print('正在处理............')
header = True
for i in csvx_list:
    fr = open(i, 'r', encoding='utf8')
    if not header:
        next(fr)
    else:
        header = False
    freadc = fr.read()
    with open(dstpath + '.csv', 'a', encoding='utf8') as f:
        f.write(freadc)
        f.write("\n")
    print('写入成功！')
print('写入完毕！')
print('10秒钟自动关闭程序！')
