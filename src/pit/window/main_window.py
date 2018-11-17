#!/usr/bin/env python3

import sys
import curses
import dateutil.parser

from typing import List

sys.path.append('../../')

from pit.window.base_window import BaseWindow
from pit.window.body_window import BodyWindow

from pit.items import Item

class MainWindow(BaseWindow):
    """
    This class manage the list.

    Gets a list and gives it behavior.
    """
    pass

    def name(self):
        return "main"

    def __init__(self, stdscr):
        super().__init__(stdscr)

    def refresh(self):
        height, width = self.stdscr.getmaxyx()
        self.pad.erase()
        for (i, item) in enumerate(self.model.list()):
            if i != self.cursor:
                self.col = 0
                self.pad.move(i, self.col)

                self.write_text(self.date_format(item.created), curses.color_pair(2))
                self.write_space()
                self.write_text(str(item.id), curses.color_pair(3))
                self.write_space()
                if item.status is not None:
                    self.write_text(item.status, curses.color_pair(6))
                    self.write_space()
                self.write_text(item.author_name, curses.color_pair(5))
                self.write_space()
                self.write_text(item.title, curses.color_pair(0))
            else:
                attr = curses.color_pair(18)
                self.pad.addstr(i, 0, self.format(item), attr)
        # TODO: Calucurate 2
        self.pad.refresh(self.offset, 0, 0, 0, height - 2, width - 1)

    def open(self, handler):
        handler.open(BodyWindow, self.select_item())

    def select_item(self):
        return self.model.content(self.model.list()[self.cursor])

    def format(self, item):
        # return "{} {} {} {}".format(item.id, item.status, item.author_name, item.title)
        created = self.date_format(item.created)
        # TODO: Adjust padding
        all_params = [created, item.id, item.status, item.author_name, item.title]
        params = [x for x in all_params if x is not None]
        count = len(params)
        format_string = '{} ' * count + ' ' * 200
        return format_string.format(*params)

    def date_format(self, date):
        return dateutil.parser.parse(date).strftime("%Y-%m-%d %H:%M %z")

