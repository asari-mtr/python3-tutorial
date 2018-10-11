#!/usr/bin/env python3

post_list = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "Auguest",
        "September",
        "Octover",
        "November",
        "December",
        ]

def refresh(pos=0):
    for n in post_list:
        print("\\e[1m%s\\e[m" % n)

def getchar():
    import sys, tty, termios

    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)
    return ch

refresh()

while True:
    ch = getchar()

    if ch == 'q':
        print("quit")
        exit(0)
    else:
        print("\e[0J")
        refresh()

