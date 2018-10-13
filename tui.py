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
    for i, v in enumerate(post_list):
        print("\33[3{}m\33[4{}m{}\33[m".format(i % 8, (i + 2) % 8, v))
    print('\33[14F')

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

clear = '\33[0J'
print(clear)
refresh()

while True:
    ch = getchar()

    if ch == 'q':
        print("quit")
        exit(0)
    else:
        print(clear)
        refresh()

