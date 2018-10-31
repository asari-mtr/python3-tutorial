#!/usr/bin/env python3

import curses
from curses import textpad
from curses import wrapper
from curses import panel
import time

from pit.handler.window_handler import WindowHandler
from pit.window.footer_window import FooterWindow
from pit.window.list_window import ListWindow

from pit.model.test_model import TestModel

def make_content(stdscr):
    height, width = stdscr.getmaxyx()
    win = stdscr.subwin(height - 1, width - int(width / 2), 0, int(width / 2))
    win.vline(curses.ACS_VLINE, height - 1)
    win.addstr(0, 2, "content")
    win.refresh()
    return win

def main(stdscr):
    "main"
    handler = WindowHandler(stdscr)

    footer = FooterWindow(stdscr)
    d_content = make_content(stdscr)
    content = ListWindow(stdscr)

    test_model = TestModel()

    key = ''
    while True:
        footer.clear()
        content.clear()

        height, width = stdscr.getmaxyx()
        footer.write_left('Hello2')
        footer.write_right("({}, {})".format(content.offset, content.cursor))

        stdscr.refresh()
        footer.refresh()


        content.set_model(test_model.list())
        content.refresh()

        key = stdscr.getch()
        if key == 0x6a: # j
            content.scroll(1)
        if key == 0x6b: # k
            content.scroll(-1)
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
            update(stdscr)

wrapper(main)
