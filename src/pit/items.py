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
    def __init__(self, item=Item()):
        self.id = item.id
        self.title = item.title
        self.body = item.body
        self.created = item.created
        self.updated = item.updated
        self.status = item.status
        self.author_id = item.author_id
        self.author_name = item.author_name
        self.link = item.link
        self.category = item.category
        self.labels = item.labels
        self.body = item.body

class Comment(AttrDict):
    pass
    # id = None
    # content = None
    # created = None
    # updated = None
    # author_id = None
    # author_name = None
