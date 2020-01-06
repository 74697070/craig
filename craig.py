#!/usr/bin/python

from craigslist import CraigslistForSale
from db import *
from sms import *
import time
import random

queries = ['steelcase', 'aeron', 'herman miller chair', 'leap', 'steelcase chair']

def search(query):
    cl_s = CraigslistForSale(site='lasvegas',category='fua', 
            filters={'zip_code': '89117', 'search_titles': True, 'posted_today': False, 'query': query, 'search_distance': '30'})

    for result in cl_s.get_results(sort_by='newest'):
        id = result['id']
        exists = fetch_query(id)
        if (not exists):
            insert_row(result['repost_of'], result['datetime'], result['url'], result['price'], result['name'], result['id'])
            conn.commit()
            row = fetch_query(id)
            text(row[2].encode('ascii', 'ignore'))

def run():
    for query in queries:
        print('searching....%s' % (query))
        search(query)
        time.sleep(random.randint(10,45))

run()
