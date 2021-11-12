#!/usr/bin/python3
# -*-coding:utf-8 -*

import sys

i = 0

for f in sys.stdin:
    f = f.strip()
    for line in f.split('\r'):
        params = line.split(',')
        price = params[2]
        country = params[7]
        print(country + "\t" + price)
