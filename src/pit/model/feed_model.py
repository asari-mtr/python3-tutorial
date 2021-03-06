# -*- coding: utf-8 -*-

import sys
import html2text

from typing import List

sys.path.append('../../')

from pit.items import Item, Content, Comment

from backlog import FeedHandler

class FeedModel:
    def name():
        return "feed"

    def __init__(self):
        url = "https://qiita.com/tags/Python/feed"
        self.handler = FeedHandler(url)
        self.items = None
        self.h = html2text.HTML2Text()
        self.h.ignore_links = True

    def define_view(self):
        return ["created", "status", "author_name", "title"]

    def list(self) -> List[Item]:
        if self.items is None:
            self.items = [self.create_item(entry) for entry in self.handler.request().entries]

        return self.items

    def create_item(self, entry):
        item = Item()
        item.id = entry.id
        item.title = entry.title
        item.created = entry.published
        item.updated = entry.updated
        item.status = None
        item.author_id = entry.author
        item.author_name = entry.author
        item.link = entry.link
        item.category = None
        item.labels = None
        item.body = self.h.handle(entry.content[0].value)

        return item

    def content(self, item: Item) -> Content:
        return Content(item)

