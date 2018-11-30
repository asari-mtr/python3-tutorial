# -*- coding: utf-8 -*-

import sys

from typing import List

sys.path.append('../../')

from pit.items import Item, Content, Comment

from backlog import GithubHandler

class GithubModel:
    def name():
        return "github"

    def __init__(self):
        self.handler = GithubHandler("asari-mtr/study-record")
        self.items = None
        self.select = 0

    def select_item(self):
        return self.items[self.select]

    def define_view(self):
        return ["created", "id", "status", "author_name", "title"]

    def list(self) -> List[Item]:
        if self.items is None:
            self.items = [self.create_item(issue) for issue in self.handler.request('issues')]

        return self.items

    def create_item(self, issue):
        item = Item()
        item.id = issue['number']
        item.title = issue['title']
        item.created = issue['created_at']
        item.updated = issue['updated_at']
        item.status = issue['state']
        item.author_id = issue['user']['login']
        item.author_name = issue['user']['login']
        item.link = issue['html_url']
        item.category = 'Issue'
        item.labels = [label['name'] for label in issue['labels']]
        item.body = issue['body']

        return item

    def content(self, item: Item) -> Content:
        return Content(item)

    def comment(self, item: Item) -> List[Comment]:
        if self.comments is None:
            self.comments = [self.create_comment(comment) for comment in self.handler.request("issues/{}/comments".format(item.id))]

        return self.comments

    def create_comment(self, i):
         comment = Comment()
         comment['id'] = i['id']
         comment['content'] = i['body']
         comment['created'] = i['created_at']
         comment['updated'] = i['updated_at']
         comment['author_id'] = i['user']['id']
         comment['author_name'] = i['user']['login']

         return comment
