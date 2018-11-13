# -*- coding: utf-8 -*-

import sys

from typing import List

sys.path.append('../../')

from pit.items import Item, Content, Comment

from backlog import GithubHandler

class GithubModel:
    def __init__(self):
        self.handler = GithubHandler("asari-mtr/study-record")
        self.items = None

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
