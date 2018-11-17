#!/usr/bin/env python3

import curses
import dateutil.parser
import subprocess
from pit.items import Item

import textwrap
from pit.window.base_window import BaseWindow

class BodyWindow(BaseWindow):
    def name(self):
        return "content"

    def __init__(self, stdscr):
        super().__init__(stdscr)
        self.pad = curses.newpad(10000, 400)
        # self.pager = False

    def date_format(self, date):
        # TODO: duplicate
        return dateutil.parser.parse(date).strftime("%Y-%m-%d %H:%M %z")

    def labels_format(self, labels):
        return " ".join(map(lambda label: "[{}]".format(label), labels))

    def open(self, handler):
        if self.model.link is not None:
            subprocess.call(['open', self.model.link])

    def pageup(self):
        height, width = self.stdscr.getmaxyx()
        # TODO: Calucurate 1
        display_height = height - 1

        self.offset = max(self.offset - display_height, 0)

    def pagedown(self):
        height, width = self.stdscr.getmaxyx()
        # TODO: Calucurate 1
        display_height = height - 1

        self.offset = min(self.offset + display_height, self.last() - display_height)

    def scroll(self, lines=1):
        height, width = self.stdscr.getmaxyx()
        # TODO: Calucurate 2
        display_height = height - 2
        if lines > 0:
            self.offset= min(self.offset+ lines, self.last())
        else:
            self.offset = max(self.offset + lines , 0)

    def refresh(self):
        height, width = self.stdscr.getmaxyx()
        #self.pad.erase()
        display_width = int(width / 2) - 1
        self.col = 1
        self.row = 0
        self.pad.move(0, 1)

        self.write_text("[{}]".format(self.model.status), curses.color_pair(6))
        self.write_space()
        self.write_text('{}/'.format(self.model.category), curses.color_pair(0))
        self.write_textn(self.model.title, curses.color_pair(0))

        self.write_space()
        self.write_text(self.date_format(self.model.created), curses.color_pair(2))
        self.write_space()
        self.write_textn(self.model.author_name, curses.color_pair(5))

        if self.model.labels is not None:
            self.write_space()
            self.write_textn(self.labels_format(self.model.labels), curses.color_pair(3))

        self.write_textn()

        lines = textwrap.dedent(self.model.body).strip().splitlines()
        for i, line in enumerate(lines):
            length = len(line)
            ps = [ line[j:min(j+display_width - 2, length)]  for j in range(0, length, display_width - 2)]
            for p in ps:
                self.write_space()
                self.write_textn(p, curses.color_pair(0))

        self.write_space()
        self.write_textn()
        self.write_textn('-' * display_width, curses.color_pair(0))
        self.write_textn()

        self.set_line_count(self.row + 1)

        if self.offset > self.last():
            self.offset = 0

        self.pad.attrset(curses.color_pair(20))
        self.pad.move(0, 0)
        self.pad.vline(curses.ACS_VLINE, self.row + height)
        self.pad.attrset(curses.color_pair(0))

        # TODO: Calucurate 2
        self.pad.refresh(self.offset, 0, 0, display_width, height - 2, width - 1)
