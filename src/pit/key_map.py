# -*- coding: utf-8 -*-

class KeyMap():
    char_maps = {
            'Enter':    0xa
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

