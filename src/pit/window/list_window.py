#!/usr/bin/env python3

import sys
import curses

from typing import List

sys.path.append('../../')

from pit.model.test_model import TestModel

from pit.items import Item

class ListWindow:
    """
    This class manage the list.

    Gets a list and gives it behavior.
    """
    pass

    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.pad = curses.newpad(100, 100)
        self.pad.scrollok(True)
        self.cursor = 0
        self.offset = 0

    def set_model(self, items: List[Item]):
        for (i, item) in enumerate(items):
            attr = curses.A_NORMAL if i != self.cursor else curses.A_REVERSE
            self.pad.addstr(i, 0, self.decorate(item), attr)

    def decorate(self, item):
        # return "{} {} {} {}".format(item.id, item.status, item.author_name, item.title)
        return "{} {} {} {}".format(item['id'], item['status'], item['author_name'], item['title'])

    def refresh(self):
        height, width = self.stdscr.getmaxyx()
        self.pad.refresh(self.offset, 0, 0, 0, height - 2, int(width / 2) - 1)

    def scroll(self, lines=1):
        height, width = self.stdscr.getmaxyx()
        absolute_y = self.cursor - self.offset
        display_height = height - 2
        if lines > 0:
            self.cursor = min(self.cursor + lines, 49)
            if absolute_y > display_height:
                self.offset = self.offset + lines
        else:
            self.cursor = max(self.cursor + lines , 0)
            if 0 > absolute_y :
                self.offset = self.offset + lines


