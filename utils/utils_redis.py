__author__ = 'ymg'
#!/usr/bin/env python3
# -*- coding: utf-8
'''
Date: 2017/02/15
Author: YMG
Description: redis utils for security-platform(sp).
'''

import redis
def redis_conn(host='127.0.0,1', port=6379, db=0, pwd=''):
    try:
        pool = redis.ConnectionPool(host=host, port=port, db=db, password=pwd)
        r = redis.Redis(connection_pool=pool)
        return r
    except BaseException as e:
        print(e)
        # logger.error(e)
        
        return ''




