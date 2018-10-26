#!/usr/bin/env python3

import os
import json
import urllib.parse
import urllib.request

from urllib.error import URLError, HTTPError

class BacklogHandler:
    def __init__(self):
        self.token = os.getenv('BACKLOG_TOKEN')
        self.team = os.getenv('BACKLOG_TEAM')
        self.endpoint = "https://{}.backlog.jp".format(self.team)

    def request(self):
        url = "{}/api/v2/issues".format(self.endpoint)
        param = "Bearer {}".format(self.token)
        req = urllib.request.Request(url, headers = {'Authorization': param}, method = "GET")
        try:
            with urllib.request.urlopen(req) as res:
                body = res.read()

                return json.loads(body)
        except HTTPError as e:
            print('Error code: %s %s' % (e.code, e.reason))
            print(e.headers)
        except URLError as e:
            print('Error opening %s' % (e.reason))

handler = BacklogHandler()
res = handler.request()
print(res)

