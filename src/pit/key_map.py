# -*- coding: utf-8 -*-

class KeyMap():
    char_maps = {
            'Enter':    0x00a,
            'Tab':      0x009,
            'Space':    0x020,
            'Lt':       0x03c,
            'Del':      0x07f,
            'Down':     0x102,
            'Up':       0x103,
            'Left':     0x104,
            'Right':    0x105,
            'F1':       0x109,
            'F2':       0x10a,
            'F3':       0x10b,
            'F4':       0x10c,
            'F5':       0x10d,
            'F6':       0x10e,
            'F7':       0x10f,
            'F8':       0x110,
            'F9':       0x111,
            'F10':      0x112,
            'F11':      0x113,
            'F12':      0x114,
    }
    def __init__(self, alias, request):
        self.alias = self.to_charcode(alias)
        self.request = request

    def to_charcode(self, alias):
        if len(alias) == 1:
            return ord(alias)

        if alias.startswith("C-") and len(alias) == 3:
            return ord(alias[-1].lower()) - 0x60

        if alias in KeyMap.char_maps:
            return KeyMap.char_maps[alias]

        raise KeyError("Not found key map: {}".format(alias))

