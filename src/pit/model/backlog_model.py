# -*- coding: utf-8 -*-

import sys

from typing import List

sys.path.append('../../')

from pit.items import Item, Content, Comment

from backlog import BacklogHandler

class BacklogModel:
    def name():
        return "github"

    def __init__(self):
        self.handler = BacklogHandler()
        self.items = None

    def define_view(self):
        return ["created", "id", "status", "author_name", "title"]

    def list(self) -> List[Item]:
        if self.items is None:
            self.items = [self.create_item(issue) for issue in self.handler.request('issues', [('statusId[]', 1), ('statusId[]', 2), ('statusId[]', 3), ('count', 100)])]

        return self.items

    def create_item(self, issue):
        item = Item()
        item.id = issue['issueKey']
        item.title = issue['summary']
        item.created = issue['created']
        item.updated = issue['updated']
        item.status = issue['status']['name']
        item.author_id = issue['createdUser']['userId']
        item.author_name = issue['createdUser']['name']
        item.link = None
        item.category = issue['issueType']['name']
        item.labels = [label for label in issue['category']]
        item.body = issue['description']

        return item

    def content(self, item: Item) -> Content:
        return Content(item)

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
