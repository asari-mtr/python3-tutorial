#!/usr/bin/env python3

import curses
from curses import wrapper

def main(stdscr):
    stdscr.clear()
    pad = curses.newpad(100, 100)

    for y in range(0, 99):
        for x in range(0, 99):
            pad.addch(y, x , ord('a') + (x * x + y * y) % 26)

    pad.refresh(5, 5, 10, 10, 20, 75)
    pad.getkey()


wrapper(main)
