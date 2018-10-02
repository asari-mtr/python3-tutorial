#!/usr/bin/env python3

import os
import sys
import json
import urllib.parse
import urllib.request
import datetime
import copy

import hashlib
import hmac
import base64

from collections import OrderedDict
from urllib.error import URLError, HTTPError

class TwHandler:
    def __init__(self):
        self.__api_key = os.getenv('TW_API_KEY')
        self.__api_secret = os.getenv('TW_API_SECRET')
        self.__access_token = os.getenv('TW_TOKEN')
        self.__access_token_secret = os.getenv('TW_SECRET')


    def __sig_param(self):
        now = datetime.datetime.now()
        return {
            'oauth_token': self.__access_token,
            'oauth_consumer_key': self.__api_key,
            'oauth_signature_method': 'HMAC-SHA1',
            'oauth_timestamp': str(int(now.timestamp())),
            'oauth_nonce': str(now.timestamp()),
            'oauth_version': '1.0',
        }


    def get_request(self, url, param):
        return self.__twitter("GET", url, param)


    def post_request(self, url, param):
        return self.__twitter("POST", url, param)


    def __twitter(self, method, url, param):
        sig_param = self.__sig_param()

        merged_param = self.__merge_param(param, sig_param)
        sig = self.__signature(method, url, merged_param)

        header_param = self.__header_param(sig, copy.deepcopy(sig_param))

        full_request_url = self.__full_request_url(url, param)

        return self.__request(full_request_url, header_param, method)

    def __signature(self, method, request_url, param):
        request_query = self.__make_request_query(param)

        encoded_list = [method, request_url, request_query]

        sig_data = '&'.join(map(lambda p: urllib.parse.quote(p, safe=""), encoded_list))
        sig_key = '&'.join(map(lambda s: urllib.parse.quote(s),  [self.__api_secret, self.__access_token_secret]))

        sha1 = hmac.new(bytes(sig_key, encoding='utf-8'), bytes(sig_data, encoding='utf-8'), hashlib.sha1).digest()

        return base64.urlsafe_b64encode(sha1).decode('ascii')


    def __full_request_url(self, url, param):
        request_query = self.__make_request_query(param)
        return url + "?" + request_query


    def __merge_param(self, request_param, sig_param):
        merged_param = { **request_param, **sig_param }

        return OrderedDict(sorted(merged_param.items(), key = lambda x:x[0]))


    def __make_request_query(self, param):
        return "&".join(["%s=%s" % (key, urllib.parse.quote(str(value), safe="")) for (key, value) in param.items()])


    def __header_param(self, sig, merged_param):
        merged_param['oauth_signature'] = sig
        merged_param = OrderedDict(sorted(merged_param.items(), key = lambda x:x[0]))
        header_param = ", ".join(["%s=\"%s\"" % (key, urllib.parse.quote(str(value))) for (key, value) in merged_param.items()])
        return "OAuth " + header_param


    def __request(self, url, param, method):
        req = urllib.request.Request(url, headers = {'Authorization': param}, method = method)
        try:
            with urllib.request.urlopen(req) as res:
                body = res.read()

            return json.loads(body)

        except HTTPError as e:
            print('Error code: %s %s' % (e.code, e.reason))
            print(e.headers)
        except URLError as e:
            print('Error opening %s' % (e.reason))


handler = TwHandler()

user = os.getenv('TW_USER')

request_url = "https://api.twitter.com/1.1/statuses/user_timeline.json"
request_param = { "screen_name": user, "include_rts": "false" , "count": 200 }

res = handler.get_request(request_url, request_param)

for line in res:
    print(line['id_str'] + "::" + line['created_at'])
    for entity in line['entities'].get('media', []):
        if entity.get('type') == 'photo':
            print(entity.get('media_url', "nothing"))

