# -*- coding:utf-8 -*-

import urllib.request
import urllib.parse
import json


from lxml.html import parse

parsed = parse(urllib.request.urlopen('https://ask.julyedu.com/'))
doc = parsed.getroot()
links = doc.findall('.//a')
urls = [lnk.get('href') for lnk in links]
links2 = doc.findall('.//h4')
questions = [val.text_content() for val in links2]
for question in questions:
    print(str(question).strip())

