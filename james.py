#!/usr/bin/env python

import random
from functools import partial

beverages = [ "red bull", "coffee" ]
languages = [ "python", "PHP", "JavaScript" ]

def caffeinate():
    print "James just sank another %s" % random.choice(beverages)

def upload_ads():
    print "James just uploaded some ads"

def code(language):
    print "James just coded in %s" % language

activities = [ caffeinate, upload_ads, partial(code, languages[0]) ]

while 1:
    random.choice(activities)()
    