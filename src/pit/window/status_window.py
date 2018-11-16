# -*- coding: utf-8 -*-

import curses

class StatusWindow:
    def __init__(self, scr):
        self.scr = scr
        self.window = scr.subwin(self.get_height(), 0)

    def write_left(self, message, attr=0):
        self.window.addstr(0, 0, message, attr)

    def write_right(self, message, attr=0):
        height, width = self.scr.getmaxyx()
        pos = width - len(message) - 1
        self.window.addstr(0, pos, message, attr)

    def clear(self):
        self.window.erase()

    def refresh(self):
        self.window.mvwin(self.get_height(), 0)
        # TODO: Move attribute
        self.window.bkgd(" ", curses.color_pair(22))
        self.window.refresh()

    def get_height(self):
        h, _w = self.scr.getmaxyx()
        return h - 1
