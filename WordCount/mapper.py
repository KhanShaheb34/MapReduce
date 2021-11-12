#!/usr/bin/python3
# -*-coding:utf-8 -*

import sys

for line in sys.stdin:
    line = line.strip()
    words = line.split()
    for word in words:
        print(word + "\t1")
