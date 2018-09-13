#!/usr/bin/python

import glob

file_list = glob.glob("*")

for file in file_list:
    print(file)
