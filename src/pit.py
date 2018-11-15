#!/usr/bin/env python3

import curses
from curses import textpad
from curses import wrapper
from curses import panel
import time

from pit.handler.key_handler import get_request
from pit.handler.window_handler import WindowHandler
from pit.window.status_window import StatusWindow
from pit.window.main_window import MainWindow

from pit.request import Request

def main(stdscr):
    "main"
    handler = WindowHandler(stdscr)

    key = 0
    request = Request.VIEW_MAIN
    while handler.view_driver(request) is None:
        height, width = stdscr.getmaxyx()
        current_window = handler.current_window()

        a = type(current_window.model)
        handler.status_left('[{}][{}]'.format(a, current_window.name()))

        current = handler.current_window()
        handler.status_right("{} ({}, {}) ({}, {}) {} {}".format(hex(key), height, width, current.offset, current.cursor, current.last(), request.name))

        handler.refresh()
        key = stdscr.getch()
        request = get_request(key)

        if key == curses.KEY_RESIZE:
            stdscr.clear()
        handler.clear()

wrapper(main)
