#!/usr/bin/env python3
# -*- coding: utf-8
"""
 _    _ _   _         _____
 | |  | | | | |       |  __ \
 | |__| | |_| |_ _ __ | |__) | __ _____  ___   _
 |  __  | __| __| '_ \|  ___/ '__/ _ \ \/ / | | |
 | |  | | |_| |_| |_) | |   | | | (_) >  <| |_| |
 |_|  |_|\__|\__| .__/|_|   |_|  \___/_/\_\\__, |
                | |                         __/ |
                |_|                        |___/
Date: 2016/01/12
Author: YMG
Description: http Proxy for security-platform(sp).
"""

from mitmproxy import controller, options, master
from mitmproxy.proxy import ProxyServer, ProxyConfig
from utils import Config
from urllib import parse


class SpProxy(master.Master):
    def run(self):
        try:
            master.Master.run(self)
        except KeyboardInterrupt:
            self.shutdown()

    @controller.handler
    #type(f) = mitmproxy.http.HTTPFlow
    def request(self, f):
        # 定义请求参数变量
        self.req_method = ''
        self.req_url = ''
        self.req_cookies = ''
        self.req_content = ''
        self.req_ua = ''
        self.req_referer = ''
        hid = (f.request.host, f.request.port)
        if "cookie" in f.request.headers:
            # YMG: get the cookie when the request contains the cookie
            self.req_cookies = f.request.headers.get_all("cookie")
        # Created by YMG 2015/12/09
        # Record the information about the request
        self.req_method = f.request.method
        self.req_url = f.request.url
        self.req_content = f.request.content
        if "Referer" in f.request.headers:
            self.req_referer = f.request.headers['Referer']
        if "User-Agent" in f.request.headers:
            self.req_ua = f.request.headers['User-Agent']
        #exclude the ext of requests
        urlext = parse.urlparse(self.req_url)[2].split('.')[-1]
        # print(urlext)
        ignoreext = ('js', 'css', 'png', 'jpg', 'gif', 'bmp', 'svg', 'exif', 'jpeg', 'exe', 'doc', 'docx', 'ppt', 'pptx', 'pdf', 'ico', 'wmv', 'avi', 'swf', 'apk', 'xml', 'xls', 'thmx')
        # req_headers = f.request.headers
        if urlext not in ignoreext:
            info = {}
            info['method'] = self.req_method
            info['cookies'] = self.req_cookies
            info['content'] = self.req_content
            info['User-Agent'] = self.req_ua
            info['referer'] = self.req_referer
            info['url'] = self.req_url
            ###Insert the info{} to redis
            #r=redis_obj.connect()
            #r.lpush('req-queue', json.dumps(info))
            print(info)


    # @controller.handler
    # def response(self, f):
    #     print("response", f)
    #
    # @controller.handler
    # def error(self, f):
    #     print("error", f)
    #
    # @controller.handler
    # def log(self, l):
    #     print("log", l.msg)

if __name__ == "__main__":
    opts = options.Options(cadir="~/.mitmproxy/")
    config = ProxyConfig(opts)
    server = ProxyServer(config)
    m = SpProxy(opts, server)
    m.run()
    # print('main')
    # prxport = Config.get_config('config.ini', 'proxy', 'port')
    # print(prxport)
