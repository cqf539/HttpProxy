__author__ = 'ymg'
# -*- coding: utf-8
'''
Date: 2016/01/12
Author: YMG
Description: get config for security-platform(sp).
'''

from configparser import *


# def getConfig(cfgfilename, section, key, logger):
def get_config(cfgfilename, section, key):
    try:
        config = ConfigParser()
        with open(cfgfilename, 'r') as cfgfile:
            config.read_file(cfgfile)
            return config.get(section, key)
    except IOError as e:
        print(e)
        # logger.error(e)
        return ''
    except NoSectionError as e:
        print(e)
        # logger.error(e)
        return ''
    except BaseException as e:
        print(e)
        # logger.error(e)
        return ''

if __name__ == "__main__":
    print('Config main')

