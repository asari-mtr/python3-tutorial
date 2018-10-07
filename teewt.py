#!/usr/bin/env python3

import time
import curses

def pbar(window):
    for i in range(10):
        window.addstr(10, 10, "[" + ("=" * i) + ">" + (" " * (10 - i )) + "]")
        window.refresh()
        time.sleep(0.5)

def main(stdscr):
    stdscr.clear()

    for i in range(0, 9):
        v = i - 10
        stdscr.addstr(i, 0, '10 divided by {} is {}'.format(v, 10/v))

    stdscr.refresh()
    key =  stdscr.getkey()
    print(key)

curses.wrapper(main)
