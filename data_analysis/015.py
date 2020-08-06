#!/usr/bin/env python3

import pandas as pd
import sys

input_file = 'supplier_data.csv'
output_file = 'outfile.csv'

data_frame = pd.read_csv(input_file,header=None)
data_frame = data_frame.drop([0,1,2,10,11,12])

data_frame.columns = data_frame.iloc[0]

data_frame = data_frame.reindex(data_frame.index.drop(3))

print(data_frame)

data_frame.to_csv(output_file, index=False)

