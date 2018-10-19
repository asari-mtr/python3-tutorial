#!/usr/bin/env python3
import sys

# http://invisible-island.net/xterm/ctlseqs/ctlseqs.html
HIDE_CURSOR = '\33[?25l'
SHOW_CURSOR = '\33[?25h'

ERASE_BELOW         = '\33[0J'
ERASE_AVOVE         = '\33[1J'
ERASE_ALL           = '\33[2J'
ERASE_SAVED_LINES   = '\33[3J'

sys.stdout.write(HIDE_CURSOR)

def clear():
    print(ERASE_BELOW)
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
        sys.stdout.write(SHOW_CURSOR)
        exit(0)
    if ch == 'j':
        pos = min(pos + 1, 11)
    if ch == 'k':
        pos = max(pos - 1, 0)

    clear()
    refresh(pos)

