#!/usr/bin/python

import re

phone = "2004-959-559 # This is Phone Number"

num = re.sub(r'#.*$', "", phone)
print("Phone num : ", num)

num = re.sub(r'\D', "", phone)
print("Phone num : ", num)
