#!/usr/bin/python

import argparse
import glob
import os
from stat import *
import pwd
import grp
import datetime

parser = argparse.ArgumentParser(description='Show file list')
parser.add_argument('-l', action='store_true', default=False, help='Show detail files list')

args = parser.parse_args()

def to_perm(mode):
    d = "-"
    if(S_ISDIR(mode)):
        d = "d"

    if(S_ISLNK(mode)):
        d = "l"

    user  = perm((mode >> 6) & 0b111)
    group = perm((mode >> 3) & 0b111)
    other = perm((mode >> 0) & 0b111)

    return f"{d}{user}{group}{other}"

def perm(i):
    r = 'r' if ((i >> 2) & 1 == 1) else '-'
    w = 'w' if ((i >> 1) & 1 == 1) else '-'
    x = 'x' if ((i >> 0) & 1 == 1) else '-'
    return f"{r}{w}{x}"

file_list = glob.glob("*")
if (args.l):
    width_size = max(map(lambda f: len(str(os.stat(f)[ST_SIZE])), file_list))
    for f in sorted(file_list):
        stat = os.lstat(f)
        mode = to_perm(stat.st_mode)
        nlink = stat.st_nlink
        uid = pwd.getpwuid(stat.st_uid)
        gid = grp.getgrgid(stat.st_gid)
        size = f"%{width_size}d" % stat.st_size
        mtime = datetime.datetime.fromtimestamp(stat.st_mtime).strftime("%m %d %H:%M")
        name = f if not os.path.islink(f) else f"{f} -> {os.readlink(f)}"
        print(f"{mode} {nlink}  {uid.pw_name}  {gid.gr_name}  {size} {mtime} {name}")
else:
    for f in file_list:
        print(f)
