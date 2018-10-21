#!/usr/bin/env python3

import curses
from curses import textpad
from curses import wrapper
import time

def update(stdscr):
    stdscr.clear()
    stdscr.border()

def main(stdscr):
    "main"
    curses.curs_set(0)

    update(stdscr)

    key = ''
    while True:
        height, width = stdscr.getmaxyx()
        stdscr.addstr(2, 2, "hello {} {}".format(height, width))
        if not key == '':
            stdscr.addstr(3, 2, "pressed {}".format(key))
        stdscr.refresh()
        key = stdscr.getch()
        if key == 0x71: # q
            break
        if key == curses.KEY_RESIZE:
            update(stdscr)

wrapper(main)
