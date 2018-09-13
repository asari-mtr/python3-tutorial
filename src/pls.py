#!/usr/bin/python

import argparse
import glob
import os
from stat import *

parser = argparse.ArgumentParser(description='Show file list')
parser.add_argument('-l', action='store_true', default=False, help='Show detail files list')

args = parser.parse_args()

def to_perm(mode):
    return mode

file_list = glob.glob("*")
if (args.l):
    for f in file_list:
        mode = to_perm(os.stat(f)[ST_MODE])
        uid = os.stat(f)[ST_UID]
        gid = os.stat(f)[ST_GID]
        size = os.stat(f)[ST_SIZE]
        ctime = os.stat(f)[ST_CTIME]
        print(f"{mode:o} {uid} {gid} {size} {ctime} {f}")
else:
    for f in file_list:
        print(f)
