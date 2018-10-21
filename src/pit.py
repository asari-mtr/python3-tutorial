#!/usr/bin/env python3

import curses
from curses import textpad
from curses import wrapper
from curses import panel
import time

def update(stdscr):
    stdscr.clear()
    stdscr.border()

def make_panel(h, w, y, x, str):
    win = curses.newwin(h, w, y, x)
    win.clear()
    win.border()
    win.addstr(2, 2, str)

    panel = curses.panel.new_panel(win)
    return win, panel

def main(stdscr):
    "main"
    curses.curs_set(0)

    update(stdscr)

    win1, panel1 = make_panel(10, 12, 5, 5, "Panel 1")
    win2, panel2 = make_panel(10, 12, 8, 8, "Panel 2")
    panel1.top()
    curses.panel.update_panels()

    key = ''
    x, y = 8, 8
    while True:
        height, width = stdscr.getmaxyx()
        stdscr.addstr(2, 2, "hello {} {}".format(height, width))
        if not key == '':
            stdscr.addstr(3, 2, "pressed {}".format(key))

        panel2.move(x, y)
        curses.panel.update_panels()
        stdscr.refresh()
        key = stdscr.getch()
        if key == 0x6a: # j
            x += 1
        if key == 0x6b: # k
            x -= 1
        if key == 0x68: # h
            y -= 1
        if key == 0x6c: # l
            y += 1
        if key == 0x71: # q
            break
        if key == curses.KEY_RESIZE:
            update(stdscr)

wrapper(main)
