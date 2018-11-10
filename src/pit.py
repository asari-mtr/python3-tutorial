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
        KeyMap('Enter',     Request.ENTER),
        KeyMap('Lt',        Request.BACK),
        KeyMap('C-n',       Request.NEXT),
        KeyMap('Down',      Request.NEXT),
        KeyMap('J',         Request.NEXT),
        KeyMap('C-p',       Request.PREVIOUS),
        KeyMap('Up',        Request.PREVIOUS),
        KeyMap('K',         Request.PREVIOUS),
        KeyMap(',',         Request.PARENT),
        KeyMap('Tab',       Request.VIEW_NEXT),
        KeyMap('R',         Request.REFRESH),
        KeyMap('F5',        Request.REFRESH),
        KeyMap('O',         Request.MAXIMIZE),
        KeyMap('q',         Request.VIEW_CLOSE),
        KeyMap('Q',         Request.QUIT),
        KeyMap('C-C',       Request.QUIT),

        KeyMap('j',         Request.MOVE_DOWN),
        KeyMap('k',         Request.MOVE_UP),
        KeyMap('C-f',       Request.MOVE_PAGE_DOWN),
        KeyMap('C-b',       Request.MOVE_PAGE_UP),
        KeyMap('C-d',       Request.MOVE_HALF_PAGE_DOWN),
        KeyMap('C-u',       Request.MOVE_HALF_PAGE_UP),
        KeyMap('g',         Request.MOVE_FIRST_LINE),
        KeyMap('G',         Request.MOVE_LAST_LINE),

        KeyMap('m',         Request.VIEW_MAIN),
        KeyMap('b',         Request.VIEW_BODY),
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
    request = Request.VIEW_MAIN
    while handler.view_driver(request) is None:
        height, width = stdscr.getmaxyx()
        current_window = handler.current_window()
        if current_window.prev_window is None:
            handler.status_left('[{}]'.format(current_window.name()))
        else:
            handler.status_left('[{} -> {}]'.format(type(current_window.prev_window), current_window.name()))
        handler.status_right("{} ({}, {}) ({}, {})".format(hex(key), height, width, handler.current_window().offset, handler.current_window().cursor))

        handler.refresh()
        key = stdscr.getch()
        request = get_request(key)

        if key == curses.KEY_RESIZE:
            stdscr.clear()
        handler.clear()

wrapper(main)
