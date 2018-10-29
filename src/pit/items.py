# -*- coding: utf-8 -*-

class AttrDict(dict):
    def __getter__(self, item):
        return self[item]

    def __dir__(self):
        return super().__dir__() + [str(k) for k in self.keys()]

class Item(AttrDict):
    pass
    # id = None
    # title = None
    # created = None
    # updated = None
    # status = None
    # author_id = None
    # author_name = None
    # category = None
    # labels = []

class Content(AttrDict):
    pass
    # id = None
    # title = None
    # body = None
    # created = None
    # updated = None
    # status = None
    # author_id = None
    # author_name = None
    # category = None
    # labels = []

class Comment(AttrDict):
    pass
    # id = None
    # content = None
    # created = None
    # updated = None
    # author_id = None
    # author_name = None
