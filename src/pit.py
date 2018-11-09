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

from pit.request import Request
from pit.key_map import KeyMap

key_maps = {
        KeyMap('Enter',     Request.OPEN),
        KeyMap('j',         Request.NEXT_LINE),
        KeyMap('k',         Request.PREV_LINE),
        KeyMap('C-n',       Request.PAGE_DOWN),
        KeyMap('C-p',       Request.PAGE_UP),
        KeyMap('C-f',       Request.HALF_PAGE_DOWN),
        KeyMap('C-b',       Request.HALF_PAGE_UP),
        KeyMap('g',         Request.MOVE_TOP),
        KeyMap('G',         Request.MOVE_BOTTOM),
        KeyMap('q',         Request.QUIT),

        KeyMap('m',         Request.MAIN_VIEW),
        KeyMap('b',         Request.BODY_VIEW),
}

def get_request(key):
    for key_map in key_maps:
        if key_map.alias == key:
            return key_map.request

    return Request.NOBIND

def main(stdscr):
    "main"
    handler = WindowHandler(stdscr)

    key = 0
    request = Request.MAIN_VIEW
    while handler.view_driver(request) is None:
        height, width = stdscr.getmaxyx()
        handler.status_left('[{}]'.format(handler.current_window().name()))
        handler.status_right("{} ({}, {}) ({}, {})".format(hex(key), height, width, handler.current_window().offset, handler.current_window().cursor))

        handler.refresh()
        key = stdscr.getch()
        request = get_request(key)

        if key == curses.KEY_RESIZE:
            stdscr.clear()
        handler.clear()

wrapper(main)
