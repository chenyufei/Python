#!/usr/bin/env python3
import csv
import glob
import os
import sys

input_path = 'E:\\chenyufei\\github\\foundations-for-analytics-with-python\\csv'
output_file = "chen_00.csv"

all_files = glob.glob(os.path.join(input_path, 'sales_*'))

output_header_list = ['file_name', 'total_sales', 'average_sales']
csv_out_file = open(output_file, 'a', newline='')
filewriter = csv.writer(csv_out_file)
filewriter.writerow(output_header_list)
for input_file in all_files:
    with open(input_file, 'r', newline='') as csv_in_file:
        filereader = csv.reader(csv_in_file)
        output_list = []
        output_list.append(os.path.basename(input_file))
        header = next(filereader)
        total_sales = 0.0
        number_of_sales = 0.0
        for row in filereader:
            sale_amount = row[3]
            total_sales += float(str(sale_amount).strip('$').replace(',', ''))
            number_of_sales += 1
        average_sales = '{0:.2f}'.format(total_sales/number_of_sales)
        output_list.append(total_sales)
        output_list.append(average_sales)
        filewriter.writerow(output_list)
        print(output_list)
csv_out_file.close()



