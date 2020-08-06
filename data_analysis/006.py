#!usr/bin/env python3

import pandas as pd
import sys

input_file = 'supplier_data.csv'
output_file = 'outfile.csv'

data_frame = pd.read_csv(input_file)
data_frame['Cost'] = data_frame['Cost'].str.strip('$').replace(',', '').astype(float)
data_frame_value_meets_condition = data_frame.loc[data_frame['Supplier Name'].str.contains('Z') | (data_frame['Cost'] > 600.0), :]
data_frame_value_meets_condition.to_csv(output_file, index=False)
print(data_frame_value_meets_condition)