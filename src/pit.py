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

from enum import IntEnum
from enum import auto


class KeyMap():
    def __init__(self, alias, request):
        self.alias = alias
        self.request = request

class Request(IntEnum):
    NONE                = auto()
    NOBIND              = auto()
    OPEN                = auto()
    NEXT_LINE           = auto()
    PREV_LINE           = auto()
    PAGE_DOWN           = auto()
    PAGE_UP             = auto()
    HALF_PAGE_DOWN      = auto()
    HALF_PAGE_UP        = auto()
    MOVE_TOP            = auto()
    MOVE_BOTTOM         = auto()
    QUIT                = auto()
    MAIN_VIEW           = auto()
    BODY_VIEW           = auto()

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

def view_driver(handler, request):
    view = handler.current_window()
    if request == Request.NOBIND:
        pass
    elif request == Request.OPEN:
        prev_window = view
        view= view.open()

    elif request == Request.NEXT_LINE:
        view.scroll(1)

    elif request == Request.PREV_LINE:
        view.scroll(-1)

    elif request == Request.PAGE_DOWN:
        win = view if view.prev_window is None else view.prev_window
        win.scroll(1)
        if view.prev_window is not None:
            view.set_model(view.prev_window.select_item())

    elif request == Request.PAGE_UP:
        win = view if view.prev_window is None else view.prev_window
        win.scroll(-1)
        if view.prev_window is not None:
            view.set_model(view.prev_window.select_item())

    elif request == Request.HALF_PAGE_UP:
        view.pageup()

    elif request == Request.HALF_PAGE_UP:
        view.pagedown()

    elif request == Request.MOVE_TOP:
        view.top()

    elif request == Request.MOVE_BOTTOM:
        view.bottom()

    elif request == Request.QUIT:
        if view.prev_window is None:
            return True
        else:
            view = view.prev_window
            view.prev_window = None

    elif request == Request.MAIN_VIEW:
        handler.open(MainWindow)

    elif request == Request.BODY_VIEW:
        handler.open(BodyWindow)

    else:
        pass

def main(stdscr):
    "main"
    handler = WindowHandler(stdscr)

    key = 0
    request = Request.MAIN_VIEW
    while view_driver(handler, request) is None:
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
