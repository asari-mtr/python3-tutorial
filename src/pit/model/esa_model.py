# -*- coding: utf-8 -*-

import sys

from typing import List

sys.path.append('../../')

from pit.items import Item, Content, Comment

from backlog import EsaHandler

class EsaModel:
    def name():
        return "esa"

    def __init__(self):
        self.handler = EsaHandler()
        self.items = None

    def list(self) -> List[Item]:
        if self.items is None:
            response = self.handler.request('posts', {'per_page': 100, 'sort': 'created'})
            self.items = [self.create_item(post) for post in response["posts"]]

        return self.items

    def create_item(self, post):
        item = Item()
        item.id = post['number']
        item.title = post['name']
        item.created = post['created_at']
        item.updated = post['updated_at']
        item.status = 'wip' if post['wip'] else None
        item.author_id = post['created_by']['name']
        item.author_name = post['created_by']['screen_name']
        item.link = post['url']
        item.category = 'category'
        item.labels = post['tags']
        item.body = post['body_md']

        return item

    def content(self, item: Item) -> Content:
        content = Content()
        content.id = item.id
        content.title = item.title
        content.body = item.body
        content.created = item.created
        content.updated = item.updated
        content.status = item.status
        content.author_id = item.author_id
        content.author_name = item.author_name
        content.link = item.link
        content.category = item.category
        content.labels = item.labels

        return content

    def comment(self, item: Item) -> List[Comment]:
        return [self.create_comment(i) for i in range(1, 20)]

    def create_comment(self, i):
         comment = Comment()
         comment['id'] = i
         comment['content'] = "Comment {}".format(i)
         comment['created'] = "2012-07-23T06:10:15Z"
         comment['updated'] = "2012-07-23T06:10:15Z"
         comment['author_id'] = 1234
         comment['author_name'] = "Test user"

         return comment
