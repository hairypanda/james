#!/usr/bin/env python

import random

beverages = [ "red bull", "coffee" ]

def caffeinate():
    print "James just sank another %s" % beverages[random.randrange(0, len(beverages))]

while [ 1 ]:
    caffeinate()
