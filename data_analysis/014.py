#!/usr/bin/env python3

import pandas as pd
import sys

input_file = 'supplier_data.csv'
output_file = 'outfile.csv'

data_frame = pd.read_csv(input_file)
data_frame_column_by_name = data_frame.loc[:, ['Invoice Number', 'Purchase Date']]
print(data_frame_column_by_name)
data_frame_column_by_name.to_csv(output_file, index=False)

