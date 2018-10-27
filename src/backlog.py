#!/usr/bin/env python3

import os
import json
import urllib.parse as urlparse
import urllib.request

from urllib.error import URLError, HTTPError
from urllib.parse import urlencode

class BacklogHandler:
    def __init__(self):
        self.token = os.getenv('BACKLOG_TOKEN')
        self.team = os.getenv('BACKLOG_TEAM')
        self.endpoint = "https://{}.backlog.jp".format(self.team)

    def request(self, action, params={}):
        url = "{}/api/v2/{}".format(self.endpoint, action)
        _params = dict(params)
        _params['apiKey'] = self.token
        url_parts = list(urlparse.urlparse(url))
        url_parts[4] = urlencode(_params)

        req = urllib.request.Request(urlparse.urlunparse(url_parts), method = "GET")
        try:
            with urllib.request.urlopen(req) as res:
                body = res.read()

                return json.loads(body)
        except HTTPError as e:
            print('Error code: %s %s' % (e.code, e.reason))
            print(e.headers)
        except URLError as e:
            print('Error opening %s' % (e.reason))

class EsaHandler:
    def __init__(self):
        self.token = os.getenv('ESA_TOKEN')
        self.team = os.getenv('ESA_TEAM')
        self.endpoint = 'https://api.esa.io'

    def request(self, action, params={}):
        url = "{}/v1/teams/{}/{}".format(self.endpoint, self.team, action)
        _params = dict(params)
        url_parts = list(urlparse.urlparse(url))
        url_parts[4] = urlencode(_params)

        req = urllib.request.Request(urlparse.urlunparse(url_parts), headers = {'Authorization': "bearer {}".format(self.token)}, method = "GET")
        try:
            with urllib.request.urlopen(req) as res:
                body = res.read()

                return json.loads(body)
        except HTTPError as e:
            print('Error code: %s %s' % (e.code, e.reason))
            print(e.headers)
        except URLError as e:
            print('Error opening %s' % (e.reason))


handler = EsaHandler()
posts = handler.request('posts', {'q': "third_web", 'per_page': 100, 'sort': 'best_match'})

for post in posts['posts']:
    print("[{}] {}".format(post['number'], post['name']))
    print(post['body_md'])

# handler = BacklogHandler()
# issues = handler.request('issues', {'projectId[]': 90134, 'statusId[]': 2, 'count': 100})
# for issue in issues:
#     print("[{}] {} {} by {}".format(issue['issueKey'], issue['summary'], issue['dueDate'], issue['createdUser']['name']))
#     comments = handler.request('issues/{}/comments'.format(issue['issueKey']), {'count': 1})
#     if len(comments) > 0:
#         comment = comments[0]['content']
#         print(comment) if comment is not None else None

