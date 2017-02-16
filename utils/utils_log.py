__author__ = 'ymg'
# -*- coding: utf-8
'''
Date: 2017/01/12
Author: YMG
Description: log function for security-platform(sp).
'''

import logging
def recordINFOlog(filename):
    log_filename = filename
    log_format = '%(asctime)s %(filename)s [line:%(lineno)d] [%(levelname)s] %(message)s'
    try:
        logging.basicConfig(level=logging.INFO, format=log_format, datefmt='%a, %d %b %Y %H:%M:%S', filename=log_filename, filemode='a')
        return logging.getLogger()
    except IOError as e:
        print(e)
        exit(1)