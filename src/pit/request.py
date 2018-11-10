# -*- coding: utf-8 -*-

from enum import IntEnum
from enum import auto

class Request(IntEnum):
    NONE                = auto()
    NOBIND              = auto()
    ENTER               = auto()
    BACK                = auto()
    NEXT                = auto()
    PREVIOUS            = auto()
    PARENT              = auto()
    MAXIMIZE            = auto()
    REFRESH             = auto()
    VIEW_NEXT           = auto()
    VIEW_CLOSE          = auto()
    QUIT                = auto()

    MOVE_DOWN           = auto()
    MOVE_UP             = auto()
    MOVE_PAGE_DOWN      = auto()
    MOVE_PAGE_UP        = auto()
    MOVE_HALF_PAGE_DOWN = auto()
    MOVE_HALF_PAGE_UP   = auto()
    MOVE_FIRST_LINE     = auto()
    MOVE_LAST_LINE      = auto()

    VIEW_MAIN           = auto()
    VIEW_BODY           = auto()
