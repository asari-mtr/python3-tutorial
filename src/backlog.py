#!/usr/bin/env python3

import os
import json
import urllib.request

from copy import deepcopy

from urllib.error import URLError, HTTPError
from urllib.parse import parse_qsl, urlencode, urlparse, urlunparse

def set_query(url, params, token=None):
    tuple_list = []
    if isinstance(params, dict):
        tuple_list = list(params.items())
    elif isinstance(params, list):
        tuple_list = params
    else:
        raise ValueError('invalid params type')

    _params = deepcopy(tuple_list)
    if token is not None:
        _params.append((token[0], token[1]))
    components = urlparse(url)
    query_pairs = parse_qsl(urlparse(url).query)
    for (f, v) in _params:
        query_pairs.append((f, v))

    new_query_str = urlencode(query_pairs)
    new_components = (
            components.scheme,
            components.netloc,
            components.path,
            components.params,
            new_query_str,
            components.fragment
    )
    return urlunparse(new_components)

def urlopen(req):
    try:
        with urllib.request.urlopen(req) as res:
            body = res.read()

            return json.loads(body)
    except HTTPError as e:
        print('Error code: %s %s' % (e.code, e.reason))
        print(e.headers)
    except URLError as e:
        print('Error opening %s' % (e.reason))

class BacklogHandler:
    def __init__(self):
        self.token = os.getenv('BACKLOG_TOKEN')
        self.team = os.getenv('BACKLOG_TEAM')
        self.endpoint = "https://{}.backlog.jp".format(self.team)

    def request(self, action, params={}):
        url = "{}/api/v2/{}".format(self.endpoint, action)

        queried_url = set_query(url, params, token = ('apiKey', self.token))

        req = urllib.request.Request(queried_url, method = "GET")
        return urlopen(req)

def bearer(token):
    return "bearer {}".format(token)

class EsaHandler:
    def __init__(self):
        self.token = os.getenv('ESA_TOKEN')
        self.team = os.getenv('ESA_TEAM')
        self.endpoint = 'https://api.esa.io'

    def request(self, action, params={}):
        url = "{}/v1/teams/{}/{}".format(self.endpoint, self.team, action)

        queried_url = set_query(url, params)

        req = urllib.request.Request(queried_url, headers = {'Authorization': bearer(self.token)}, method = "GET")
        return urlopen(req)


# handler = EsaHandler()
# posts = handler.request('posts', {'q': "third_web", 'per_page': 100, 'sort': 'best_match'})
# 
# for post in posts['posts']:
#     print("[{}] {}".format(post['number'], post['name']))
#     print(post['body_md'])

handler = BacklogHandler()
issues = handler.request('issues', [('projectId[]', 90134), ('statusId[]', 1), ('statusId[]', 2), ('count', 100)])
issues = handler.request('issues', {'projectId[]': 90134, 'statusId[]': 1, 'count': 100})
for issue in issues:
    print("[{}] ({}) {} {} by {}".format(issue['issueKey'], issue['status']['name'], issue['summary'], issue['dueDate'], issue['createdUser']['name']))
    comments = handler.request('issues/{}/comments'.format(issue['issueKey']), [('count', 1)])
    if len(comments) > 0:
        comment = comments[0]['content']
        print(comment) if comment is not None else None

