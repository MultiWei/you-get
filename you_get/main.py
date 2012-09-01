#!/usr/bin/env python

__all__ = ['main', 'any_download', 'any_download_playlist']

from .downloader import *
from .common import *

def url_to_module(url):
    site = r1(r'http://([^/]+)/', url)
    assert site, 'invalid url: ' + url
    
    if site.endswith('.com.cn'):
        site = site[:-3]
    domain = r1(r'(\.[^.]+\.[^.]+)$', site)
    assert domain, 'unsupported url: ' + url
    
    k = r1(r'([^.]+)', domain)
    downloads = {
        '56': w56,
        'cntv': cntv,
        'iqiyi': iqiyi,
        'ku6': ku6,
        'pptv': pptv,
        'sohu': sohu,
        'tudou': tudou,
        'yinyuetai': yinyuetai,
        'youku': youku,
        'youtube': youtube,
        #TODO:
        # 'acfun': acfun,
        # 'bilibili': bilibili,
        # 'kankanews': bilibili,
        # 'iask': iask,
        # 'sina': iask,
    }
    if k in downloads:
        return downloads[k]
    else:
        raise NotImplementedError(url)

def any_download(url, output_dir = '.', merge = True, info_only = False):
    m = url_to_module(url)
    m.download(url, output_dir = output_dir, merge = merge, info_only = info_only)

def any_download_playlist(url, output_dir = '.', merge = True, info_only = False):
    m = url_to_module(url)
    m.download_playlist(url, output_dir = output_dir, merge = merge, info_only = info_only)

def main():
    import sys
    try:
        script_main('you-get', any_download, any_download_playlist)
    except KeyboardInterrupt:
        sys.exit(1)
