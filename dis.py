#!/usr/bin/python

import dis;

def sum():
    vara = 10
    varb = 20

    sum = vara + varb
    print ("vara + varb = %d" % sum)

dis.dis(sum)
