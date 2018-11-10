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

    def open(self, window, model=None):
        if not (window.name in self.views.keys()):
            self.views[window.name] = window(self.stdscr)
        view = self.views[window.name]
        if model is not None:
            view.model = model
        if len(self.displayed) > 0:
            view.prev_window = self.current_window()
        self.displayed.append(view)
        self.change_window()
        self.stdscr.refresh()
        self.refresh()

    def current_window(self):
        if len(self.displayed) == 0 or self.current_window_index > len(self.displayed):
            return None

        return self.displayed[self.current_window_index]

    def change_window(self):
        if len(self.displayed) < 2:
            return

        self.current_window_index = 1 - self.current_window_index

    def status_left(self, msg):
        self.status_window.write_left(msg)

    def status_right(self, msg):
        self.status_window.write_right(msg)

    def clear(self):
        self.current_window().clear()
        self.status_window.clear()

    def refresh(self):
        for view in self.displayed:
            view.refresh()
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
           view.open(self)

       elif request == Request.VIEW_NEXT:
           self.change_window()

       elif request == Request.NEXT:
           if view.prev_window is not None:
               view.prev_window.scroll(1)
               item = view.prev_window.select_item()
               view.model = item
           else:
               view.scroll(1)

       elif request == Request.PREVIOUS:
           if view.prev_window is not None:
               view.prev_window.scroll(-1)
               item = view.prev_window.select_item()
               view.model = item
           else:
               view.scroll(-1)

       elif request in [Request.QUIT, Request.VIEW_CLOSE]:
           if view.prev_window is None:
               return True
           else:
               self.displayed.pop()
               self.current_window_index = 0

       elif request == Request.VIEW_MAIN:
           self.open(MainWindow)

       elif request == Request.VIEW_BODY:
           self.open(BodyWindow)

       elif view.pager:
           self.pager_driver(view, request)


    def pager_driver(self, view, request):
       if request == Request.MOVE_DOWN:
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

       else:
           pass
