#!/usr/bin/env python3

import pandas as pd
import sys

input_file = 'supplier_data.csv'
output_file = 'outfile.csv'

data_frame = pd.read_csv(input_file)
data_frame_column_by_index = data_frame.iloc[:, [0, 3]]
print(data_frame_column_by_index)
data_frame_column_by_index.to_csv(output_file, index=False)

