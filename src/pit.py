#!/usr/bin/env python3

import curses
from curses import textpad
from curses import wrapper
from curses import panel
import time

from pit.handler.window_handler import WindowHandler
from pit.window.footer_window import FooterWindow

def make_content(stdscr):
    height, width = stdscr.getmaxyx()
    win = stdscr.subwin(height - 1, width - int(width / 2), 0, int(width / 2))
    win.vline(curses.ACS_VLINE, height - 1)
    win.addstr(0, 2, "content")
    win.refresh()

    win2 = curses.newpad(100, 100)
    win2.scrollok(True)

    return win2

def get_window_status(stdscr):
    height, width = stdscr.getmaxyx()
    status = "({}, {})".format(height, width)
    return (status, width - len(status) - 1)

def main(stdscr):
    "main"
    handler = WindowHandler(stdscr)

    footer = FooterWindow(stdscr)
    content = make_content(stdscr)

    key = ''
    offset = 0
    cursor = 0
    while True:
        footer.clear()

        height, width = stdscr.getmaxyx()
        footer.write_left('Hello2')
        footer.write_right("({}, {})".format(offset, cursor))

        stdscr.refresh()
        footer.refresh()
        for n in range(0, 50):
            attr = curses.A_NORMAL if n != cursor else curses.A_REVERSE
            content.addstr(n, 0, "{} 1234567890".format(n), attr)
        content.refresh(offset, 0, 0, 0, height - 2, int(width / 2) - 1)
        key = stdscr.getch()
        display_height = height - 2
        if key == 0x6a: # j
            cursor = min(cursor + 1, 49)
            absolute_y = cursor - offset
            if absolute_y > display_height:
                offset += 1

        if key == 0x6b: # k
            cursor = max(cursor - 1, 0)
            absolute_y = cursor - offset
            if absolute_y < 0:
                offset -= 1
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
