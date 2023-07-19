#!/usr/bin/env python3
""" web cache module """

import redis
import requests
from datetime import timedelta


def get_page(url: str) -> str:
    """
    """
    rredis = redis.Redis()
    key = "count:{}{}{}".format('{', url, '}')
    rredis.incr(key)
    res = requests.get(url)
    rredis.setex(url, timedelta(seconds=10), res.text)
    return res.text


if __name__ == '__main__':
    get_page('http://slowwly.robertomurray.co.uk')
