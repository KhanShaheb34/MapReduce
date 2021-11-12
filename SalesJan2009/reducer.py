#!/usr/bin/python3
# -*-coding:utf-8 -*

from operator import itemgetter
import sys

current_country = None
current_price = 0
country = None

for line in sys.stdin:
    line = line.strip()
    country, price = line.split('\t', 1)

    try:
        price = int(price)
    except ValueError:
        continue
    
    if current_country == country:
        current_price += price
    else:
        if current_country:
            print(current_country + "\t" + str(current_price))
        current_price = price
        current_country = country

if current_country == country:
    print(current_country + "\t" + str(current_price))
