# -*- coding: utf-8 -*-

from enum import IntEnum
from enum import auto

class Request(IntEnum):
    NONE                = auto()
    NOBIND              = auto()
    OPEN                = auto()
    NEXT_LINE           = auto()
    PREV_LINE           = auto()
    PAGE_DOWN           = auto()
    PAGE_UP             = auto()
    HALF_PAGE_DOWN      = auto()
    HALF_PAGE_UP        = auto()
    MOVE_TOP            = auto()
    MOVE_BOTTOM         = auto()
    QUIT                = auto()
    MAIN_VIEW           = auto()
    BODY_VIEW           = auto()
