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
    main_window.set_model(test_model)

    key = 0
    current_window = main_window
    prev_window = None
    while True:
        status.clear()
        if prev_window is not None:
            prev_window.clear()
        current_window.clear()

        height, width = stdscr.getmaxyx()
        status.write_left('[{}]'.format(current_window.name()))
        status.write_right("{} ({}, {}) ({}, {})".format(hex(key), height, width, current_window.offset, current_window.cursor))

        stdscr.refresh()
        status.refresh()

        if prev_window is not None:
            prev_window.refresh()

        current_window.refresh()

        key = stdscr.getch()
        if key == 0xa: # Enter
            prev_window = current_window
            current_window = current_window.open()
        if key == 0x2f: # /
            pass
        if key == 0x3a: # :
            pass
        if key == 0x6a: # j
            current_window.scroll(1)
        if key == 0x6b: # k
            current_window.scroll(-1)
        if key == 0xe: # C-n
            win = current_window if prev_window is None else prev_window
            win.scroll(1)
            if prev_window is not None:
                current_window.set_model(prev_window.select_item())
        if key == 0x10: # C-p
            win = current_window if prev_window is None else prev_window
            win.scroll(-1)
            if prev_window is not None:
                current_window.set_model(prev_window.select_item())
        if key == 0x2: # C-b
            current_window.pageup()
        if key == 0x6: # C-f
            current_window.pagedown()
        if key == 0x6c: # l
            pass
        if key == 0x68: # h
            pass
        if key == 0x67: # g
            current_window.top()
        if key == 0x47: # G
            current_window.bottom()
        if key == 0x75: # u
            pass
        if key == 0x71: # q
            if prev_window is None:
                break
            else:
                current_window = prev_window
                prev_window = None
        if key == curses.KEY_RESIZE:
            stdscr.clear()

wrapper(main)
