#!/usr/bin/python

import argparse
import glob
import os
from stat import *
import pwd
import grp

parser = argparse.ArgumentParser(description='Show file list')
parser.add_argument('-l', action='store_true', default=False, help='Show detail files list')

args = parser.parse_args()

def to_perm(mode):
    d = "-"
    if(S_ISDIR(mode)):
        d = "d"
    return f"{d}{mode}"

file_list = glob.glob("*")
if (args.l):
    for f in file_list:
        mode = to_perm(os.stat(f)[ST_MODE])
        stat = os.stat(f)
        uid = pwd.getpwuid(stat[ST_UID])
        gid = grp.getgrgid(stat[ST_GID])
        size = stat[ST_SIZE]
        ctime = stat[ST_CTIME]
        print(f"{mode} {uid.pw_name} {gid.gr_name} {size} {ctime} {f}")
else:
    for f in file_list:
        print(f)
