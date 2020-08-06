#!usr/bin/env python3

import pandas as pd
import sys
import csv

input_file = 'supplier_data.csv'
output_file = 'outfile.csv'

my_columns = [0, 2, 3]
with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)
        header = next(filereader)
        filewriter.writerow(header)

        for row_list in filereader:
            row_list_output = []
            for index_value in my_columns:
                row_list_output.append(row_list[index_value])
            print(row_list_output)
            filewriter.writerow(row_list_output)