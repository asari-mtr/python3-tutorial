# -*- coding: utf-8 -*-

import curses

class FooterWindow:
    def __init__(self, scr):
        self.scr = scr
        height, width = scr.getmaxyx()
        self.window = scr.subwin(height - 1, 0)

    def write_left(self, message, attr=0):
        self.window.addstr(0, 0, message, attr)

    def write_right(self, message, attr=0):
        height, width = self.scr.getmaxyx()
        pos = width - len(message) - 1
        self.window.addstr(0, pos, message, attr)

    def clear(self):
        self.window.erase()

    def refresh(self):
        height, width = self.scr.getmaxyx()
        self.window.mvwin(height - 1, 0)
        # TODO: Move attribute
        self.window.bkgd(" ", curses.color_pair(1))
        self.window.refresh()
