# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod

import curses

from pit.model.github_model import GithubModel

class BaseWindow(ABC):

    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.pad = curses.newpad(100, 400)
        self.pad.scrollok(True)
        self.cursor = 0
        self.offset = 0
        self.model = GithubModel()
        self.prev_window = None
        self.pager = True
        super().__init__()

    def clear(self):
        self.pad.erase()

    @abstractmethod
    def refresh(self):
        pass

    @abstractmethod
    def open(self, handler):
        pass

    def top(self):
        self.scroll(-1000)

    def bottom(self):
        self.scroll(1000)

    def pageup(self):
        height, width = self.stdscr.getmaxyx()
        # TODO: Calucurate 1
        display_height = height - 1

        self.cursor = max(self.cursor - display_height, 0)
        self.offset = self.cursor

    def pagedown(self):
        height, width = self.stdscr.getmaxyx()
        # TODO: Calucurate 1
        display_height = height - 1

        last = len(self.model.list()) - 1
        self.cursor = min(self.cursor + display_height, last)
        if self.offset + display_height < last:
            self.offset = self.cursor

    def scroll(self, lines=1):
        height, width = self.stdscr.getmaxyx()
        # TODO: Calucurate 2
        display_height = height - 2
        last = len(self.model.list()) - 1
        if lines > 0:
            self.cursor = min(self.cursor + lines, last)
            absolute_y = self.cursor - self.offset
            if absolute_y > display_height:
                self.offset = min(self.offset + lines, last - display_height)
        else:
            self.cursor = max(self.cursor + lines , 0)
            absolute_y = self.cursor - self.offset
            if 0 > absolute_y :
                self.offset = max(self.offset + lines, 0)

