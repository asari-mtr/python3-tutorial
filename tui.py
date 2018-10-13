#!/usr/bin/env python3
import sys

sys.stdout.write('\33[?25l')

def clear():
    print('\33[0J')
    move(2)

def move(amount):
    print('\33[%sF' % amount)

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
    for i, v in enumerate(post_list):
        if pos == i:
            print("\33[1m{}\33[m".format(v))
        else:
            #print("\33[3{}m\33[4{}m{}\33[m".format(i % 8, (i + 2) % 8, v))
            print("{}".format(v))
    move(len(post_list) + 1)

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

pos = 0

while True:
    ch = getchar()

    if ch == 'q':
        print("quit")
        sys.stdout.write('\33[?25h')
        exit(0)
    if ch == 'j':
        pos = min(pos + 1, 11)
    if ch == 'k':
        pos = max(pos - 1, 0)

    clear()
    refresh(pos)

