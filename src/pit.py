#!/usr/bin/env python3

import curses
from curses import textpad
from curses import wrapper
from curses import panel
import time

def update(stdscr):
    stdscr.clear()

def make_panel(h, w, y, x, s):
    win = curses.newwin(h, w, y, x)
    win.clear()
    if h > 1:
        win.border()
        win.addstr(2, 2, s)
    else:
        win.addstr(0, 2, s)

    panel = curses.panel.new_panel(win)
    return win, panel

def init_color():
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, 7, 23)

def make_footer(stdscr):
    height, width = stdscr.getmaxyx()
    return stdscr.subwin(height - 1, 0)

def make_content(stdscr):
    height, width = stdscr.getmaxyx()
    win = stdscr.subwin(height - 1, width - int(width / 2), 0, int(width / 2))
    win.vline(curses.ACS_VLINE, height - 1)
    win.addstr(0, 2, "content")

    win2 = stdscr.subwin(int(height / 2) - 1, width - int(width / 2), int(height / 2), int(width / 2))
    win2.hline(0, 1, curses.ACS_HLINE, int(width / 2) - 1)
    win2.addstr(1, 2, "content")

    return win

def get_window_status(stdscr):
    height, width = stdscr.getmaxyx()
    status = "({}, {})".format(height, width)
    return (status, width - len(status) - 1)

def main(stdscr):
    "main"
    init_color()
    curses.curs_set(0)

    update(stdscr)

    footer = make_footer(stdscr)
    content = make_content(stdscr)

    curses.panel.update_panels()

    key = ''
    while True:
        height, width = stdscr.getmaxyx()
        footer.mvwin(height - 1, 0)
        footer.bkgd(" ", curses.color_pair(1))
        footer.addstr(0, 0, "Hello")
        window_status, pos = get_window_status(stdscr)
        footer.addstr(0, pos, window_status)

        stdscr.refresh()
        footer.refresh()
        content.refresh()
        key = stdscr.getch()
        if key == 0x6a: # j
            pass
        if key == 0x6b: # k
            pass
        if key == 0x6c: # l
            pass
        if key == 0x68: # h
            pass
        if key == 0x75: # u
            pass
        if key == 0x71: # q
            break
        if key == curses.KEY_RESIZE:
            update(stdscr)

wrapper(main)
