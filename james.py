#!/usr/bin/env python

import random

beverages = [ "red bull", "coffee" ]

def caffeinate():
    print "James just sank another %s" % random.choice(beverages)

while 1:
    caffeinate()
