#!usr/bin/env python3

import pandas as pd
import sys
import csv

input_file = 'supplier_data.csv'
output_file = 'outfile.csv'

important_dates = ['1/20/14', '1/30/14']
with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)
        header = next(filereader)
        filewriter.writerow(header)

        for row_list in filereader:
            a_date = row_list[4]
            if a_date in important_dates:
                filewriter.writerow(row_list)
                print(row_list)

