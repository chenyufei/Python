#!/usr/bin/env python3

import pandas as pd
import sys

input_file = 'supplier_data.csv'
output_file = 'outfile.csv'

data_frame = pd.read_csv(input_file)
data_frame_value_matched_pattern = data_frame.loc[data_frame['Invoice Number'].str.startswith("001-"), :]
print(data_frame_value_matched_pattern)
data_frame_value_matched_pattern.to_csv(output_file, index=False)
