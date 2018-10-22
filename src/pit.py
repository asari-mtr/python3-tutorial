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

def main(stdscr):
    "main"
    init_color()
    curses.curs_set(0)

    update(stdscr)

    win1, panel1 = make_panel(5, 20, 15, 15, "Panel 1")
    win2, panel2 = make_panel(5, 20, 18, 18, "Panel 2")
    # tb = curses.textpad.Textbox(win1)
    # text = tb.edit() # terminate with ^G
    # stdscr.addstr(7, 0, text)

    height, width = stdscr.getmaxyx()
    sub = stdscr.subwin(height - 1, 0)

    curses.panel.update_panels()

    key = ''
    current_panel = panel1
    y, x = win1.getbegyx()
    while True:
        current_panel.move(y, x)
        curses.panel.update_panels()
        height, width = stdscr.getmaxyx()
        stdscr.addstr(2, 2, "hello {} {}".format(height, width))
        if not key == '':
            stdscr.addstr(3, 2, "pressed {}({})".format(key, hex(key)))
        stdscr.addstr(4, 2, "panel1 {}".format(win1.getbegyx()))
        stdscr.addstr(5, 2, "panel2 {}".format(win2.getbegyx()))
        sub.mvwin(height - 1, 0)
        sub.bkgd(" ", curses.color_pair(1))
        sub.addstr(0, 0, "Hello")

        stdscr.refresh()
        sub.refresh()
        key = stdscr.getch()
        h, w = current_panel.window().getmaxyx()
        if key == 0x6a: # j
            y = min(height - h - 1, y + 1)
            # y += min(y - h, y + 1)
        if key == 0x6b: # k
            y = max(0, y - 1)
        if key == 0x6c: # l
            x = min(width - w, x + 1)
            # x = min(x - w, x + 1)
        if key == 0x68: # h
            x = max(0, x - 1)
        if key == 0x75: # u
            current_panel = curses.panel.bottom_panel()
            current_panel.top()
            y, x = current_panel.window().getbegyx()
        if key == 0x71: # q
            break
        if key == curses.KEY_RESIZE:
            update(stdscr)

wrapper(main)
