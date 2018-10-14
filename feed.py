#!/usr/bin/env python3

import feedparser

feed = feedparser.parse("https://qiita.com/tags/python/feed")

for entry in feed.entries:
    print("%s [%s] (%s)" % (entry.title, entry.author, entry.url))
