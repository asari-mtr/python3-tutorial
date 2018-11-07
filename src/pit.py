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

class KeyMap():
    def __init__(self, alias, request):
        self.alias = alias
        self.request = request

key_maps = {
        KeyMap(0xa,     Request.OPEN),              # Enter
        KeyMap(0x6a,    Request.NEXT_LINE),         # j
        KeyMap(0x6b,    Request.PREV_LINE),         # k
        KeyMap(0xe,     Request.PAGE_DOWN),         # C-n
        KeyMap(0x10,    Request.PAGE_UP),           # C-p
        KeyMap(0x6,     Request.HALF_PAGE_DOWN),    # C-f
        KeyMap(0x2,     Request.HALF_PAGE_UP),      # C-b
        KeyMap(0x67,    Request.MOVE_TOP),          # g
        KeyMap(0x47,    Request.MOVE_BOTTOM),       # G
        KeyMap(0x71,    Request.QUIT),              # q

        KeyMap(0x6d,    Request.MAIN_VIEW),         # m
        KeyMap(0x62,    Request.BODY_VIEW),         # b
}

def get_request(key):
    for key_map in key_maps:
        if key_map.alias == key:
            return key_map.request

    return Request.NOBIND

def open_main_view(view):
    pass

def open_body_view(view):
    pass


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
