#!/usr/bin/env python3

import os
import urllib.parse
import datetime
from collections import OrderedDict

request_url = "https://api.twitter.com/1.1/statuses/user_timeline.json"

user = os.getenv('TW_USER')
api_key = os.getenv('TW_API_KEY')
api_secret = os.getenv('TW_API_SECRET')
access_token = os.getenv('TW_TOKEN')
access_token_secret = os.getenv('TW_SECRET')

request_param = { "screen_name": "@{}".format(user), "count": 10 }

sig_key = urllib.parse.quote(api_secret) + '&' + urllib.parse.quote(access_token_secret)

now = datetime.datetime.now()

sig_param = {
        'oauth_token': access_token,
        'oauth_consumer_key': api_key,
        'oauth_signature_method': 'HMAC-SHA1',
        'oauth_timestamp': int(now.timestamp()),
        'oauth_nonce': now.timestamp(),
        'oauth_version': '1.0',
        }

merged_param = { **request_param, **sig_param }
merged_param = OrderedDict(sorted(merged_param.items(), key = lambda x:x[0]))

print(merged_param)
print(sig_key)
