#!/usr/bin/env python3

import sys
import curses
import dateutil.parser

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
        self.pad = curses.newpad(100, 400)
        self.pad.scrollok(True)
        self.cursor = 0
        self.offset = 0

    def set_model(self, items: List[Item]):
        # FIXME: Is there any other good way?
        self.pad.erase()
        for (i, item) in enumerate(items):
            if i != self.cursor:
                created = dateutil.parser.parse(item['created']).strftime("%Y-%m-%d %H:%M:%S")
                col = 0
                self.pad.addstr(i, col, created, curses.color_pair(2))
                col += len(created) + 1
                self.pad.addstr(i, col, str(item['id']), curses.color_pair(3))
                col += len(str(item['id'])) + 1
                self.pad.addstr(i, col, item['status'], curses.color_pair(4))
                col += len(item['status']) + 1
                self.pad.addstr(i, col, item['author_name'], curses.color_pair(5))
                col += len(item['author_name']) + 1
                self.pad.addstr(i, col, item['title'], curses.color_pair(0))
                col += len(item['title']) + 1
            else:
                attr = curses.color_pair(1)
                self.pad.addstr(i, 0, self.format(item), attr)

    def format(self, item):
        # return "{} {} {} {}".format(item.id, item.status, item.author_name, item.title)
        created = dateutil.parser.parse(item['created']).strftime("%Y-%m-%d %H:%M:%S")
        # TODO: Adjust padding
        return "{} {} {} {} {}{}".format(created, item['id'], item['status'], item['author_name'], item['title'], ' ' * 200)

    def refresh(self):
        height, width = self.stdscr.getmaxyx()
        # TODO: Calucurate 2
        self.pad.refresh(self.offset, 0, 0, 0, height - 2, int(width / 2) - 1)

    def scroll(self, lines=1):
        height, width = self.stdscr.getmaxyx()
        # TODO: Calucurate 2
        display_height = height - 2
        if lines > 0:
            # TODO: Calucurate 49
            self.cursor = min(self.cursor + lines, 49)
            absolute_y = self.cursor - self.offset
            if absolute_y > display_height:
                self.offset = self.offset + lines
        else:
            self.cursor = max(self.cursor + lines , 0)
            absolute_y = self.cursor - self.offset
            if 0 > absolute_y :
                self.offset = self.offset + lines


