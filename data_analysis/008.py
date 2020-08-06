#!usr/bin/env python3

import pandas as pd
import sys

input_file = 'supplier_data.csv'
output_file = 'outfile.csv'

important_dates = ['1/20/14', '1/30/14']

data_frame = pd.read_csv(input_file)
data_frame_value_in_set = data_frame.loc[data_frame['Purchase Date'].isin(important_dates), :]
print(data_frame_value_in_set)
data_frame_value_in_set.to_csv(output_file, index=False)

