#!/usr/bin/env python3

import curses
from curses import textpad
from curses import wrapper
from curses import panel
import time

from pit.handler.window_handler import WindowHandler
from pit.window.status_window import StatusWindow
from pit.window.list_window import ListWindow

from pit.model.test_model import TestModel

def main(stdscr):
    "main"
    handler = WindowHandler(stdscr)

    status = StatusWindow(stdscr)
    content = ListWindow(stdscr)

    test_model = TestModel()

    key = 0
    while True:
        status.clear()
        content.clear()

        height, width = stdscr.getmaxyx()
        status.write_left('Hello2')
        status.write_right("{} ({}, {}) ({}, {})".format(hex(key), height, width, content.offset, content.cursor))

        stdscr.refresh()
        status.refresh()

        content.set_model(test_model.list())
        content.refresh()

        key = stdscr.getch()
        if key == 0xa: # Enter
            pass
        if key == 0x2f: # /
            pass
        if key == 0x3a: # :
            pass
        if key == 0x6a: # j
            content.scroll(1)
        if key == 0xe: # C-n
            content.scroll(1)
        if key == 0x6b: # k
            content.scroll(-1)
        if key == 0x10: # C-p
            content.scroll(-1)
        if key == 0x2: # C-b
            content.pageup()
        if key == 0x6: # C-f
            content.pagedown()
        if key == 0x6c: # l
            pass
        if key == 0x68: # h
            pass
        if key == 0x67: # g
            content.top()
        if key == 0x47: # G
            content.bottom()
        if key == 0x75: # u
            pass
        if key == 0x71: # q
            break
        if key == curses.KEY_RESIZE:
            stdscr.clear()

wrapper(main)
