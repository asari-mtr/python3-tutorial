#!/usr/bin/env python3

import sys
import curses
from curses import textpad
from curses import wrapper
from curses import panel

sys.path.append('../../')

from pit.window.list_window import ListWindow

class WindowHandler:
    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.init_color()
        curses.curs_set(0)
        self.update()

    def update(self):
        self.stdscr.clear()

    def init_color(self):
        curses.start_color()
        curses.use_default_colors()
        curses.init_pair(1, 7, 23)
        curses.init_pair(2, 6, 0)
        curses.init_pair(3, 5, 0)
        curses.init_pair(4, 4, 0)
        curses.init_pair(5, 3, 0)
        curses.init_pair(6, 2, 0)
