#!/usr/bin/env python3

import curses
import dateutil.parser
import subprocess
from pit.items import Item

import textwrap
from pit.window.base_window import BaseWindow

class ItemType(IntEnum):
    NONE                = auto()
    ID                  = auto()
    TITLE               = auto()
    CREATED             = auto()
    UPDATED             = auto()
    STATUS              = auto()
    AUTHOR_ID           = auto()
    AUTHOR_NAME         = auto()
    CATEGORY            = auto()
    LINK                = auto()
    BODY                = auto()
    LABELS              = auto()

item_map = {
    "id":                       ItemType.ID,
    "title":                    ItemType.TITLE,
    "created":                  ItemType.CREATED,
    "updated":                  ItemType.UPDATED,
    "status":                   ItemType.STATUS,
    "author_id":                ItemType.AUTHOR_ID,
    "author_name":              ItemType.AUTHOR_NAME,
    "category":                 ItemType.CATEGORY,
    "link":                     ItemType.LINK,
    "body":                     ItemType.BODY,
    "labels":                   ItemType.LABELS,
}

item_style_map = {
    ItemType.ID                  : 3,
    ItemType.TITLE               : 0,
    ItemType.CREATED             : 2,
    ItemType.UPDATED             : 2,
    ItemType.STATUS              : 6,
    ItemType.AUTHOR_ID           : 5,
    ItemType.AUTHOR_NAME         : 5,
    ItemType.CATEGORY            : 0,
    ItemType.LINK                : 3,
    ItemType.BODY                : 0,
    ItemType.LABELS              : 3,
}

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
        if self.select_item().link is not None:
            subprocess.call(['open', self.select_item().link])

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

        item = self.model.select_item()
        self.write_text("[{}]".format(item.status), curses.color_pair(6))
        self.write_space()
        self.write_text('{}/'.format(item.category), curses.color_pair(0))
        self.write_textn(item.title, curses.color_pair(0))

        self.write_space()
        self.write_text(self.date_format(item.created), curses.color_pair(2))
        self.write_space()
        self.write_textn(item.author_name, curses.color_pair(5))

        if item.labels is not None:
            self.write_space()
            self.write_textn(self.labels_format(item.labels), curses.color_pair(3))

        self.write_textn()

        lines = textwrap.dedent(item.body).strip().splitlines()
        for i, line in enumerate(lines):
            length = len(line)
            ps = [ line[j:min(j+display_width - 2, length)]  for j in range(0, length, display_width - 2)]
            for p in ps:
                self.write_space()
                self.write_textn(p, curses.color_pair(0))

        self.write_space()
        self.write_textn()
        self.write_textn('-' * display_width, curses.color_pair(0))

        comments = self.model.comment(item)
        for comment in comments:
            self.write_space()
            self.write_textn("{} {}".format(comment['author_name'], comment['created']), curses.color_pair(0))
            self.write_space()
            self.write_textn(comment['content'], curses.color_pair(0))
            self.write_textn()
            self.write_textn('-' * display_width, curses.color_pair(0))

        self.set_line_count(self.row + 1)

        if self.offset > self.last():
            self.offset = 0

        # vline
        self.pad.attrset(curses.color_pair(20))
        self.pad.move(0, 0)
        self.pad.vline(curses.ACS_VLINE, self.row + height)
        self.pad.attrset(curses.color_pair(0))

        # TODO: Calucurate 2
        self.pad.refresh(self.offset, 0, 0, display_width, height - 2, width - 1)

    def get_item(self, item,  key):
        text = None
        if key in ("created"):
            text = self.date_format(item.created)
        elif key in ("id"):
            text = str(item.id)
        elif key in ("status"):
            text = item.status
        elif key in ("author_name"):
            text = item.author_name
        elif key in ("title"):
            text = item.title

        attr = None
        if key in item_map.keys():
            attr = item_style_map[item_map[key]]

        return text, attr
