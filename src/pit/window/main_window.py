#!/usr/bin/env python3

import sys
import curses
import dateutil.parser

from typing import List

sys.path.append('../../')

from pit.window.base_window import BaseWindow
from pit.window.body_window import BodyWindow

from pit.items import Item
from enum import IntEnum, auto

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

                for key in self.model.define_view():
                    text, attr = self.get_item(item, key)
                    if text is not None:
                        self.write_text(text, curses.color_pair(attr))
                        self.write_space()

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

    def get_item(self,item,  key):
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
