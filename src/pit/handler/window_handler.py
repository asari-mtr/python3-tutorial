#!/usr/bin/env python3

import sys
import curses
from curses import textpad
from curses import wrapper
from curses import panel

sys.path.append('../../')

from pit.window.main_window import MainWindow
from pit.window.status_window import StatusWindow
from pit.request import Request

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

    def view_driver(self, request):
       view = self.current_window()
       if request == Request.NOBIND:
           pass

       elif request == Request.ENTER:
           prev_window = view
           view = view.open(self)
           self.current_window()

       elif request == Request.NEXT:
           view.scroll(1)

       elif request == Request.PREVIOUS:
           view.scroll(-1)

       elif request == Request.MOVE_DOWN:
           view.scroll(1)

       elif request == Request.MOVE_UP:
           view.scroll(-1)

       elif request == Request.MOVE_PAGE_UP:
           view.pageup()

       elif request == Request.MOVE_PAGE_DOWN:
           view.pagedown()

       elif request == Request.MOVE_PAGE_DOWN:
           win = view if view.prev_window is None else view.prev_window
           win.scroll(1)
           if view.prev_window is not None:
               view.set_model(view.prev_window.select_item())

       elif request == Request.MOVE_PAGE_UP:
           win = view if view.prev_window is None else view.prev_window
           win.scroll(-1)
           if view.prev_window is not None:
               view.set_model(view.prev_window.select_item())

       elif request == Request.MOVE_FIRST_LINE:
           view.top()

       elif request == Request.MOVE_LAST_LINE:
           view.bottom()

       elif request in [Request.QUIT, Request.VIEW_CLOSE]:
           if view.prev_window is None:
               return True
           else:
               view = view.prev_window
               view.prev_window = None

       elif request == Request.VIEW_MAIN:
           self.open(MainWindow)

       elif request == Request.VIEW_BODY:
           self.open(BodyWindow)

       else:
           pass
