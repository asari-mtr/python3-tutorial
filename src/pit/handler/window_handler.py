#!/usr/bin/env python3

import sys
import curses
from curses import textpad
from curses import wrapper
from curses import panel

sys.path.append('../../')

from pit.window.main_window import MainWindow
from pit.window.status_window import StatusWindow

class WindowHandler:
    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.init_color()
        curses.curs_set(0)
        self.update()
        self.current_window_index = 0
        self.displayed = []
        self.views = {}
        self.status_window = StatusWindow(stdscr)


    def open(self, window):
        if not (window.name in self.views.keys()):
            self.views[window.name] = window(self.stdscr)
        self.displayed.append(self.views[window.name])
        self.stdscr.refresh()
        self.refresh()

    def current_window(self):
        if len(self.displayed) == 0 or self.current_window_index > len(self.displayed):
            return None

        return self.displayed[self.current_window_index]

    def status_left(self, msg):
        self.status_window.write_left(msg)

    def status_right(self, msg):
        self.status_window.write_right(msg)

    def clear(self):
        self.current_window().clear()
        self.status_window.clear()

    def refresh(self):
        self.current_window().refresh()
        self.status_window.refresh()
        self.stdscr.refresh()

    def update(self):
        self.stdscr.clear()

    def init_color(self):
        curses.start_color()
        curses.use_default_colors()
        for n in range(0, 15):
            curses.init_pair(n, n, 0)
        for n in range(16, 31):
            curses.init_pair(n, 15, n % 16)
