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


    def sig_param(self):
        now = datetime.datetime.now()
        return {
            'oauth_token': self.__access_token,
            'oauth_consumer_key': self.__api_key,
            'oauth_signature_method': 'HMAC-SHA1',
            'oauth_timestamp': str(int(now.timestamp())),
            'oauth_nonce': str(now.timestamp()),
            'oauth_version': '1.0',
        }


handler = TwHandler()

user = os.getenv('TW_USER')
api_key = os.getenv('TW_API_KEY')
api_secret = os.getenv('TW_API_SECRET')
access_token = os.getenv('TW_TOKEN')
access_token_secret = os.getenv('TW_SECRET')

request_url = "https://api.twitter.com/1.1/statuses/user_timeline.json"
method = "GET"
request_param = { "screen_name": user, "include_rts": "false" , "count": 200 }

sig_param = handler.sig_param()


def merge_param(request_param, sig_param):
    merged_param = { **request_param, **sig_param }

    return OrderedDict(sorted(merged_param.items(), key = lambda x:x[0]))

def make_request_query(merged_param):
    return "&".join(["%s=%s" % (key, urllib.parse.quote(str(value), safe="")) for (key, value) in merged_param.items()])

def signature(method, request_url, request_query):
    encoded_merged_param = urllib.parse.quote(request_query, safe="")

    encoded_request_method = urllib.parse.quote(method)
    encoded_request_url = urllib.parse.quote(request_url, safe="")

    sig_data = encoded_request_method + '&' + encoded_request_url + '&' + encoded_merged_param

    sig_key = urllib.parse.quote(api_secret) + '&' + urllib.parse.quote(access_token_secret)

    sha1 = hmac.new(bytes(sig_key, encoding='utf-8'), bytes(sig_data, encoding='utf-8'), hashlib.sha1).digest()

    return  base64.urlsafe_b64encode(sha1).decode('ascii')

def header_param(sig, merged_param):
    merged_param['oauth_signature'] = sig
    merged_param = OrderedDict(sorted(merged_param.items(), key = lambda x:x[0]))
    header_param = ", ".join(["%s=\"%s\"" % (key, urllib.parse.quote(str(value))) for (key, value) in merged_param.items()])
    return "OAuth " + header_param


def full_request_url(request_url, request_query):
    return request_url + "?" + request_query

merged_param = merge_param(request_param, sig_param)
request_query = make_request_query(merged_param)
request_query2 = make_request_query(request_param)
sig = signature(method, request_url, request_query)
header_param = header_param(sig, copy.deepcopy(sig_param))

full_request_url = full_request_url(request_url, request_query2)

import json
req = urllib.request.Request(full_request_url, headers = {'Authorization': header_param})
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
