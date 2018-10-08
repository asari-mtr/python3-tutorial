#!/usr/bin/env python3

import curses
from curses import wrapper

def main(stdscr):
    stdscr.addstr(0, 0, "Current mode: Typing mode", curses.A_BLINK)
    stdscr.addstr(1, 0, "Current mode: Typing mode", curses.A_BOLD)
    stdscr.addstr(2, 0, "Current mode: Typing mode", curses.A_DIM)
    stdscr.addstr(3, 0, "Current mode: Typing mode", curses.A_REVERSE)
    stdscr.addstr(4, 0, "Current mode: Typing mode", curses.A_STANDOUT)
    stdscr.addstr(5, 0, "Current mode: Typing mode", curses.A_UNDERLINE)
    stdscr.addstr(6, 0, "Current mode: Typing mode", curses.color_pair(1))
    stdscr.refresh()
    pad = curses.newpad(100, 100)

    for y in range(0, 99):
        for x in range(0, 99):
            pad.addch(y, x , ord('a') + (x * x + y * y) % 26)

    pad.refresh(5, 5, 10, 10, 20, 75)
    while True:
        key = pad.getkey()
        if ('q' == key):
            break

        stdscr.addstr(7, 0, "Current mode: Typing mode {}" .format(key))
        stdscr.refresh()

wrapper(main)
