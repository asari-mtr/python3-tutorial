#!/usr/bin/env python3

import curses
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

    def refresh(self):
        height, width = self.stdscr.getmaxyx()
        self.pad.vline(curses.ACS_VLINE, height - 1)
        self.pad.addstr(0, 2, self.item['title'], curses.color_pair(0))
        self.pad.addstr(1, 2, self.item['created'], curses.color_pair(2))
        self.pad.addstr(1, 30 - len(self.item['status']), self.item['status'], curses.color_pair(6))
        lines = textwrap.dedent(self.item['body']).strip().splitlines()
        for i, line in enumerate(lines):
            self.pad.addstr(i + 3, 2, line, curses.color_pair(0))
        # TODO: Calucurate 2
        self.pad.refresh(self.offset, 0, 0, int(width / 2) - 1, height - 2, width - 1)

    def name(self):
        return "content"

    def clear(self):
        self.pad.erase()
