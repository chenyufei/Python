#!/usr/bin/env python3
import sys
import glob
import os


# READ A FILE
# Read a single text file
input_file = sys.argv[1]

## Read a text file (older method) ##
print("Output #141:")
filereader = open(input_file, 'r', newline='')
for row in filereader:
    print("{}".format(row.strip()))
filereader.close()

## Read a text file (newer method) ##
print("Output #142:")
with open(input_file, 'r', newline='') as filereader:
    for row in filereader:
        print("{}".format(row.strip()))

print("Output #143:")
# READ MULTIPLE FILES
# Read multiple text files
inputPath = sys.argv[1]
for input_file in glob.glob(os.path.join(inputPath, '*.txt')):
    with open(input_file, 'r', newline='') as filereader:
       for row in filereader:
           print("{}".format(row.strip()))