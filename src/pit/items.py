# -*- coding: utf-8 -*-

class AttrDict(dict):
    def __getter__(self, item):
        return self[item]

    def __dir__(self):
        return super().__dir__() + [str(k) for k in self.keys()]

class Item(AttrDict):
    def __init__(self):
        self.id = None
        self.title = None
        self.created = None
        self.updated = None
        self.status = None
        self.author_id = None
        self.author_name = None
        self.category = None
        self.link = None
        self.body = None
        self.labels = []

class Content(AttrDict):
    def __init__(self):
        self.id = None
        self.title = None
        self.body = None
        self.created = None
        self.updated = None
        self.status = None
        self.author_id = None
        self.author_name = None
        self.category = None
        self.link = None
        self.body = None
        self.labels = []

class Comment(AttrDict):
    pass
    # id = None
    # content = None
    # created = None
    # updated = None
    # author_id = None
    # author_name = None
