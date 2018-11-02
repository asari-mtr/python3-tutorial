#!/usr/bin/env python3

import curses
from curses import textpad
from curses import wrapper
from curses import panel
import time

from pit.handler.window_handler import WindowHandler
from pit.window.status_window import StatusWindow
from pit.window.main_window import MainWindow

from pit.model.test_model import TestModel

def main(stdscr):
    "main"
    handler = WindowHandler(stdscr)

    status = StatusWindow(stdscr)
    main_window = MainWindow(stdscr)

    test_model = TestModel()

    key = 0
    while True:
        status.clear()
        main_window.clear()

        height, width = stdscr.getmaxyx()
        status.write_left('Hello2')
        status.write_right("{} ({}, {}) ({}, {})".format(hex(key), height, width, main_window.offset, main_window.cursor))

        stdscr.refresh()
        status.refresh()

        main_window.set_model(test_model.list())
        main_window.refresh()

        key = stdscr.getch()
        if key == 0xa: # Enter
            main_window.open()
        if key == 0x2f: # /
            pass
        if key == 0x3a: # :
            pass
        if key == 0x6a: # j
            main_window.scroll(1)
        if key == 0xe: # C-n
            main_window.scroll(1)
        if key == 0x6b: # k
            main_window.scroll(-1)
        if key == 0x10: # C-p
            main_window.scroll(-1)
        if key == 0x2: # C-b
            main_window.pageup()
        if key == 0x6: # C-f
            main_window.pagedown()
        if key == 0x6c: # l
            pass
        if key == 0x68: # h
            pass
        if key == 0x67: # g
            main_window.top()
        if key == 0x47: # G
            main_window.bottom()
        if key == 0x75: # u
            pass
        if key == 0x71: # q
            break
        if key == curses.KEY_RESIZE:
            stdscr.clear()

wrapper(main)
