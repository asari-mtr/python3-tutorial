# -*- coding: utf-8 -*-

from pit.key_map import KeyMap
from pit.request import Request

key_maps = {
        KeyMap('Enter',     Request.ENTER),
        KeyMap('Lt',        Request.BACK),
        KeyMap('C-n',       Request.NEXT),
        KeyMap('Down',      Request.NEXT),
        KeyMap('J',         Request.NEXT),
        KeyMap('C-p',       Request.PREVIOUS),
        KeyMap('Up',        Request.PREVIOUS),
        KeyMap('K',         Request.PREVIOUS),
        KeyMap(',',         Request.PARENT),
        KeyMap('Tab',       Request.VIEW_NEXT),
        KeyMap('R',         Request.REFRESH),
        KeyMap('O',         Request.MAXIMIZE),
        KeyMap('q',         Request.VIEW_CLOSE),
        KeyMap('Q',         Request.QUIT),
        KeyMap('C-c',       Request.QUIT),

        KeyMap('j',         Request.MOVE_DOWN),
        KeyMap('k',         Request.MOVE_UP),
        KeyMap('C-f',       Request.MOVE_PAGE_DOWN),
        KeyMap('C-b',       Request.MOVE_PAGE_UP),
        KeyMap('C-d',       Request.MOVE_HALF_PAGE_DOWN),
        KeyMap('C-u',       Request.MOVE_HALF_PAGE_UP),
        KeyMap('g',         Request.MOVE_FIRST_LINE),
        KeyMap('G',         Request.MOVE_LAST_LINE),

        KeyMap('m',         Request.VIEW_MAIN),
        KeyMap('F1',        Request.VIEW_GITHUB),
        KeyMap('F2',        Request.VIEW_TWITTER),
        KeyMap('F3',        Request.VIEW_FEED),
        KeyMap('F4',        Request.VIEW_BACKLOG),
        KeyMap('F5',        Request.VIEW_ESA),
}

def get_request(key):
    for key_map in key_maps:
        if key_map.alias == key:
            return key_map.request

    return Request.NOBIND
