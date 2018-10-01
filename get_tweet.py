#!/usr/bin/env python3

import os
import sys
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
        method = "GET"
        sig_param = self.__sig_param()
        merged_param = self.merge_param(param, sig_param)
        request_query = self.make_request_query(merged_param)
        request_query2 = self.make_request_query(param)
        sig = self.signature(method, url, request_query)
        header_param = self.header_param(sig, copy.deepcopy(sig_param))
        full_request_url = self.full_request_url(url, request_query2)
        self.tweet(full_request_url, header_param)

    def merge_param(self, request_param, sig_param):
        merged_param = { **request_param, **sig_param }

        return OrderedDict(sorted(merged_param.items(), key = lambda x:x[0]))

    def make_request_query(self, param):
        return "&".join(["%s=%s" % (key, urllib.parse.quote(str(value), safe="")) for (key, value) in param.items()])

    def signature(self, method, request_url, request_query):
        encoded_merged_param = urllib.parse.quote(request_query, safe="")

        encoded_request_method = urllib.parse.quote(method)
        encoded_request_url = urllib.parse.quote(request_url, safe="")

        sig_data = encoded_request_method + '&' + encoded_request_url + '&' + encoded_merged_param

        sig_key = urllib.parse.quote(self.__api_secret) + '&' + urllib.parse.quote(self.__access_token_secret)

        sha1 = hmac.new(bytes(sig_key, encoding='utf-8'), bytes(sig_data, encoding='utf-8'), hashlib.sha1).digest()

        return  base64.urlsafe_b64encode(sha1).decode('ascii')

    def header_param(self, sig, merged_param):
        merged_param['oauth_signature'] = sig
        merged_param = OrderedDict(sorted(merged_param.items(), key = lambda x:x[0]))
        header_param = ", ".join(["%s=\"%s\"" % (key, urllib.parse.quote(str(value))) for (key, value) in merged_param.items()])
        return "OAuth " + header_param

    def full_request_url(self, request_url, request_query):
        return request_url + "?" + request_query

    def tweet(self, url, param):
        import json
        req = urllib.request.Request(url, headers = {'Authorization': param})
        try:
            with urllib.request.urlopen(req) as res:
                body = res.read()

            timeline = json.loads(body)

            for line in timeline:
                print(line['id_str'] + "::" + line['created_at'])
                for entity in line['entities'].get('media', []):
                    if entity.get('type') == 'photo':
                        print(entity.get('media_url', "nothing"))

        except HTTPError as e:
            print('Error code: %s %s' % (e.code, e.reason))
            print(e.headers)
        except URLError as e:
            print('Error opening %s' % (e.reason))


handler = TwHandler()

user = os.getenv('TW_USER')

request_url = "https://api.twitter.com/1.1/statuses/user_timeline.json"
request_param = { "screen_name": user, "include_rts": "false" , "count": 200 }

handler.get_request(request_url, request_param)
