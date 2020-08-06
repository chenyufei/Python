# encoding:utf-8
import xlwt
import codecs
import os


def Txt_to_Excel(inputTxt, sheetName, start_row, start_col, outputExcel):
    fr = codecs.open(inputTxt, 'r', encoding='utf-8')
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet(sheetName)

    line_number = 0  # 记录有多少行，相当于写入excel时的i，
    row_excel = start_row
    for line in fr:
        line_number += 1
        row_excel += 1
        line = line.strip()
        line = line.split('\t')
        len_line = len(line)  # list中每一行有多少个数，相当于写入excel中的j
        col_excel = start_col
        for j in range(len_line):
            ws.write(row_excel, col_excel, line[j])
            col_excel += 1
            wb.save(outputExcel)


if __name__ == '__main__':
    os.chdir(u'E:/pycharm/Test/profile/')
    print('开始执行')
    sheetName = 'app'  # 需要写入excel中的Sheet2中，可以自己设定
    start_row = 0  # 从第0行开始写
    start_col = 0  # 从第0列开始写
    inputfile = 'app.txt'  # 输入文件
    outputExcel = 'excel_result.xls'  # 输出excel文件
    Txt_to_Excel(inputfile, sheetName, start_row, start_col, outputExcel)
    print('完成')
    sheetName = 'attribute'  # 需要写入excel中的Sheet2中，可以自己设定
    start_row = 0  # 从第7行开始写
    start_col = 0  # 从第3列开始写
    inputfile = 'attribute.txt'  # 输入文件
    outputExcel = 'excel_result.xls'  # 输出excel文件
    Txt_to_Excel(inputfile, sheetName, start_row, start_col, outputExcel)
    print('完成')

    sheetName = 'keyword'  # 需要写入excel中的Sheet2中，可以自己设定
    start_row = 0  # 从第7行开始写
    start_col = 0  # 从第3列开始写
    inputfile = 'keyword.txt'  # 输入文件
    outputExcel = 'excel_result.xls'  # 输出excel文件
    Txt_to_Excel(inputfile, sheetName, start_row, start_col, outputExcel)
    print('完成')

    sheetName = 'star'  # 需要写入excel中的Sheet2中，可以自己设定
    start_row = 0  # 从第7行开始写
    start_col = 0  # 从第3列开始写
    inputfile = 'star.txt'  # 输入文件
    outputExcel = 'excel_result.xls'  # 输出excel文件
    Txt_to_Excel(inputfile, sheetName, start_row, start_col, outputExcel)
    print('完成')