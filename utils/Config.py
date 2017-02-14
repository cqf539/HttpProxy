__author__ = 'ymg'
# -*- coding: utf-8
"""
Date: 2016/01/12
Author: YMG
Description: log functions for security-platform(sp).
"""

from configparser import *


# def getConfig(cfgfilename, section, key, logger):
def get_config(cfgfilename, section, key):
    try:
        config = ConfigParser()
        with open(cfgfilename, 'r') as cfgfile:
            config.read_file(cfgfile)
            return config.get(section, key)
    except IOError as e:
        print('IOError')
        print(e)
        # logger.error(e)
        return ''
    except NoSectionError as e:
        print('NoSection')
        print(e)
        # logger.error(e)
        return ''
    except BaseException as e:
        print('Base')
        print(e)
        # logger.error(e)
        return ''


if __name__ == "__main__":
    print('main')
    prxport = get_config('config.ini', 'proxy', 'port')
    print(prxport)

