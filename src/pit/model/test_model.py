# -*- coding: utf-8 -*-

import sys

from typing import List

sys.path.append('../../')

from pit.items import Item, Content, Comment

class TestModel:
    def __init__(self):
        pass

    def list(self) -> List[Item]:
        return [self.create_item(i) for i in range(1, 50)]

    def create_item(self, i):
        item = Item()
        item['id'] = i
        item['title'] = "Title {}".format(i)
        item['created'] = "2012-07-23T06:10:15Z"
        item['updated'] = "2012-07-23T06:10:15Z"
        item['status'] = "open"
        item['author_id'] = 1234
        item['author_name'] = "Test user"
        item['category'] = "Tips"
        item['labels'] = ["tips", "python"]

        return item

    def content(self, item: Item) -> Content:
        content = Content()
        content['id'] = item['id']
        content['title'] = item['title']
        content['body'] = """
         This reference manual describes the syntax and “core semantics” 
        of the language. It is terse, but attempts to be exact and complete.
         The semantics of non-essential built-in object types and of 
        the built-in functions and modules are described in The Python 
        Standard Library. 
         For an informal introduction to the language, see The Python Tutorial. 
         For C or C++ programmers, two additional manuals exist: Extending and 
        Embedding the Python Interpreter describes the high-level picture of 
        how to write a Python extension module, and the Python/C API Reference 
        Manual describes the interfaces available to C/C++ programmers in detail.
        """
        content['created'] = item['created']
        content['updated'] = item['updated']
        content['status'] = item['status']
        content['author_id'] = item['author_id']
        content['author_name'] = item['author_name']
        content['category'] = item['category']
        content['labels'] = item['labels']

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
