#!/usr/bin/env python3

import sys
import feedparser
import html2text

args = sys.argv
h = html2text.HTML2Text()

if len(args) > 1:
    tag = args[1]
else:
    tag = 'python'

rss= feedparser.parse("https://qiita.com/tags/%s/feed" % tag)

print("%s %s %s (%s)" % (rss.feed.title, rss.feed.link, rss.feed.description, rss.feed.updated))
for entry in rss.entries[1:4]:
    print(" %s %s \33[1m%s\33[0m by %s (%s)" % (entry.id, entry.published, entry.title, entry.author, entry.url))
    print(" %s" % (entry.content[0].value))
    print(" %s" % (h.handle(entry.content[0].value)))
