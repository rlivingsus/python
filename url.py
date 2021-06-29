#!/usr/bin/python

import urllib
from lxml import html

url = "x.x.x.x:1234"
page = html.fromstring(urllib.urlopen(url).read())
print page
