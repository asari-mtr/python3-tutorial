#!/usr/bin/env python3

import curses
import dateutil.parser
from pit.items import Item

import textwrap

class ContentWindow:
    def __init__(self, stdscr, item):
        self.stdscr = stdscr
        self.pad = curses.newpad(100, 400)
        self.pad.scrollok(True)
        self.cursor = 0
        self.offset = 0
        self.set_model(item)
        self.refresh()

    def set_model(self, item: Item):
        self.item = item

    def date_format(self, date):
        # TODO: duplicate
        return dateutil.parser.parse(date).strftime("%Y-%m-%d %H:%M %z")

    def labels_format(self, labels):
        return " ".join(map(lambda label: "[{}]".format(label), labels))

    def refresh(self):
        height, width = self.stdscr.getmaxyx()
        offset_x = 1

        self.pad.attrset(curses.color_pair(20))
        self.pad.vline(curses.ACS_VLINE, height - 1)
        self.pad.attrset(curses.color_pair(0))
        self.pad.addstr(0, offset_x, "[{}]".format(self.item['status']), curses.color_pair(6))
        self.pad.addstr(' ')
        self.pad.addstr('{}/'.format(self.item['category']), curses.color_pair(0))
        self.pad.addstr(self.item['title'], curses.color_pair(0))
        self.pad.addstr(1, offset_x, self.date_format(self.item['created']), curses.color_pair(2))
        self.pad.addstr(' ')
        self.pad.addstr(self.item['author_name'], curses.color_pair(5))
        self.pad.addstr(2, offset_x, self.labels_format(self.item['labels']), curses.color_pair(3))
        lines = textwrap.dedent(self.item['body']).strip().splitlines()
        for i, line in enumerate(lines):
            self.pad.addstr(i + 4, offset_x, line, curses.color_pair(0))

        offset_y = 5 + len(lines)
        self.pad.addstr(offset_y, offset_x + 1, '-' * (int(width / 2) - 1), curses.color_pair(0))

        # TODO: Calucurate 2
        self.pad.refresh(self.offset, 0, 0, int(width / 2) - 1, height - 2, width - 1)

    def name(self):
        return "content"

    def clear(self):
        self.pad.erase()
