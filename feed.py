#!/usr/bin/env python3

import sys
import feedparser

args = sys.argv

if len(args) > 1:
    tag = args[1]
else:
    tag = 'python'

rss= feedparser.parse("https://qiita.com/tags/%s/feed" % tag)

print("%s %s %s (%s)" % (rss.feed.title, rss.feed.link, rss.feed.description, rss.feed.updated))
for entry in rss.entries:
    print(" %s %s \33[1m%s\33[0m by %s (%s)" % (entry.id, entry.published, entry.title, entry.author, entry.url))
